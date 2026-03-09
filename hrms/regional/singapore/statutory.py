"""
Singapore statutory file generators:
1. CPF e-Submission file (CSV for CPF Board)
2. IR8A year-end tax file (for IRAS)
3. GIRO bank payment file (DBS/OCBC/UOB format)
4. Itemized Payslip PDF (MOM-compliant)
"""
import frappe
from frappe.utils import flt, getdate, formatdate, fmt_money
from frappe import _


# =============================================================================
# 1. CPF E-SUBMISSION FILE
# =============================================================================
# Format: CSV that employers upload to CPF e-Submit@web
# Ref: https://www.cpf.gov.sg/employer/making-cpf-contributions/how-to-make-cpf-contributions

@frappe.whitelist()
def generate_cpf_file(month, year, company="HRDL8"):
    """Generate CPF submission CSV for a given month.
    Returns dict with filename and file content."""
    start = f"{year}-{int(month):02d}-01"
    end = getdate(start)
    # Get last day of month
    if int(month) == 12:
        end = f"{year}-12-31"
    else:
        end = f"{year}-{int(month)+1:02d}-01"

    slips = frappe.get_all("Salary Slip",
        filters={
            "company": company,
            "start_date": (">=", start),
            "start_date": ("<=", end),
            "docstatus": 1,
        },
        fields=["name", "employee", "employee_name", "start_date", "gross_pay"]
    )

    lines = []
    # Header
    lines.append("CPFSUBMISSION")
    lines.append(f"Payment Month,{int(month):02d}/{year}")

    # Column headers
    lines.append("Employee ID,Employee Name,Ordinary Wages,Additional Wages,Employee CPF,Employer CPF")

    from hrms.regional.singapore.cpf import sg_cpf_employee, sg_cpf_employer

    for slip in slips:
        ss = frappe.get_doc("Salary Slip", slip.name)
        emp = frappe.get_doc("Employee", slip.employee)

        ow = flt(ss.gross_pay)
        # Calculate CPF from employee data (more reliable than reading slip deductions)
        ecpf = sg_cpf_employee(ow, emp.date_of_birth, emp.sg_pr_status)
        ercpf = sg_cpf_employer(ow, emp.date_of_birth, emp.sg_pr_status)

        lines.append(f"{emp.name},{emp.employee_name},{ow:.2f},0.00,{ecpf:.2f},{ercpf:.2f}")

    # Summary
    total_ecpf = sum(flt(l.split(",")[4]) for l in lines[3:] if "," in l)
    total_ercpf = sum(flt(l.split(",")[5]) for l in lines[3:] if "," in l)
    lines.append(f"TOTAL,,,, {total_ecpf:.2f},{total_ercpf:.2f}")

    content = "\n".join(lines)
    filename = f"CPF_Submission_{year}_{int(month):02d}.csv"

    return {"filename": filename, "content": content, "records": len(slips)}


# =============================================================================
# 2. IR8A YEAR-END TAX FILE
# =============================================================================
# IR8A: Return of Employee's Remuneration for the year
# Filed to IRAS by 1 March each year for the preceding year

@frappe.whitelist()
def generate_ir8a(year, company="HRDL8"):
    """Generate IR8A data for all employees for a given year."""
    year = int(year)
    employees = frappe.get_all("Employee",
        filters={"company": company, "status": "Active"},
        fields=["name", "employee_name", "date_of_birth", "date_of_joining",
                "designation", "sg_pr_status"]
    )

    records = []
    for emp in employees:
        # Get all submitted salary slips for this employee in the year
        slips = frappe.get_all("Salary Slip",
            filters={
                "employee": emp.name,
                "start_date": (">=", f"{year}-01-01"),
                "end_date": ("<=", f"{year}-12-31"),
                "docstatus": 1,
            },
            fields=["name"]
        )

        from hrms.regional.singapore.cpf import sg_cpf_employee, sg_cpf_employer

        total_gross = 0
        total_ecpf = 0
        total_ercpf = 0
        total_bonus = 0

        for slip_ref in slips:
            ss = frappe.get_doc("Salary Slip", slip_ref.name)
            total_gross += flt(ss.gross_pay)
            total_ecpf += sg_cpf_employee(flt(ss.gross_pay), emp.date_of_birth, emp.sg_pr_status)
            total_ercpf += sg_cpf_employer(flt(ss.gross_pay), emp.date_of_birth, emp.sg_pr_status)

        records.append({
            "employee_id": emp.name,
            "employee_name": emp.employee_name,
            "id_type": "NRIC/FIN",
            "date_of_birth": str(emp.date_of_birth) if emp.date_of_birth else "",
            "date_of_commencement": str(emp.date_of_joining) if emp.date_of_joining else "",
            "designation": emp.designation or "",
            "residency_status": emp.sg_pr_status or "Singapore Citizen",
            "gross_remuneration": flt(total_gross, 2),
            "bonus": flt(total_bonus, 2),
            "employee_cpf": flt(total_ecpf, 2),
            "employer_cpf": flt(total_ercpf, 2),
            "total_income": flt(total_gross, 2),
        })

    # Generate CSV
    lines = []
    lines.append("IR8A Return of Employee's Remuneration")
    lines.append(f"Year of Assessment,{year + 1}")
    lines.append(f"Basis Year,{year}")
    lines.append(f"Company,{company}")
    lines.append("")
    lines.append("Employee ID,Name,DOB,Date Commenced,Designation,Residency,"
                 "Gross Remuneration,Bonus,Employee CPF,Employer CPF,Total Income")

    for r in records:
        lines.append(
            f"{r['employee_id']},{r['employee_name']},{r['date_of_birth']},"
            f"{r['date_of_commencement']},{r['designation']},{r['residency_status']},"
            f"{r['gross_remuneration']:.2f},{r['bonus']:.2f},"
            f"{r['employee_cpf']:.2f},{r['employer_cpf']:.2f},{r['total_income']:.2f}"
        )

    content = "\n".join(lines)
    filename = f"IR8A_{year}_YA{year+1}.csv"

    return {"filename": filename, "content": content, "records": len(records)}


# =============================================================================
# 3. GIRO BANK PAYMENT FILE
# =============================================================================
# Standard GIRO file format for Singapore banks (DBS/OCBC/UOB)
# Used for bulk salary crediting

@frappe.whitelist()
def generate_giro_file(month, year, company="HRDL8", bank_format="DBS"):
    """Generate GIRO payment file for salary crediting."""
    start = f"{year}-{int(month):02d}-01"
    end = f"{year}-{int(month)+1:02d}-01" if int(month) < 12 else f"{year}-12-31"

    slips = frappe.get_all("Salary Slip",
        filters={
            "company": company,
            "start_date": (">=", start),
            "start_date": ("<=", end),
            "docstatus": 1,
        },
        fields=["name", "employee", "employee_name", "net_pay", "bank_name", "bank_account_no"]
    )

    value_date = f"{year}{int(month):02d}28"  # Payment date: 28th of month
    lines = []

    if bank_format == "DBS":
        # DBS GIRO format
        # Header
        lines.append(f"HEADER,GIRO,{value_date},{len(slips)}")

        total = 0
        for slip in slips:
            emp = frappe.get_doc("Employee", slip.employee)
            bank_code = emp.bank_name or ""
            account = emp.bank_account_no or ""
            amount = flt(slip.net_pay, 2)
            total += amount

            lines.append(
                f"DETAIL,{bank_code},{account},{emp.employee_name},{amount:.2f},SALARY {int(month):02d}/{year}"
            )

        lines.append(f"TRAILER,{len(slips)},{total:.2f}")

    elif bank_format == "OCBC":
        # OCBC GIRO format
        lines.append(f"H,GIRO PAYMENT,{value_date}")
        total = 0
        for slip in slips:
            emp = frappe.get_doc("Employee", slip.employee)
            amount = flt(slip.net_pay, 2)
            total += amount
            lines.append(
                f"D,{emp.bank_account_no or ''},{emp.employee_name},{amount:.2f},SAL{int(month):02d}{year}"
            )
        lines.append(f"T,{len(slips)},{total:.2f}")

    else:
        # Generic CSV format (works for most banks)
        lines.append("Bank Code,Account Number,Employee Name,Amount,Reference")
        total = 0
        for slip in slips:
            emp = frappe.get_doc("Employee", slip.employee)
            amount = flt(slip.net_pay, 2)
            total += amount
            lines.append(
                f"{emp.bank_name or ''},{emp.bank_account_no or ''},{emp.employee_name},{amount:.2f},SALARY-{int(month):02d}{year}"
            )
        lines.append(f"TOTAL,,, {total:.2f},")

    content = "\n".join(lines)
    filename = f"GIRO_{bank_format}_{year}_{int(month):02d}.csv"

    return {"filename": filename, "content": content, "records": len(slips), "total": total}


# =============================================================================
# 4. ITEMIZED PAYSLIP (MOM-COMPLIANT)
# =============================================================================
# Singapore Employment Act requires itemized payslips with:
# - Full name, date of payment, basic salary, allowances
# - Deductions (CPF, etc.), overtime, net pay, pay period

@frappe.whitelist()
def get_payslip_data(salary_slip_name):
    """Get structured payslip data for rendering."""
    ss = frappe.get_doc("Salary Slip", salary_slip_name)
    emp = frappe.get_doc("Employee", ss.employee)
    company = frappe.get_doc("Company", ss.company)

    earnings = []
    for e in ss.earnings:
        earnings.append({"component": e.salary_component, "amount": flt(e.amount, 2)})

    deductions_employee = []
    deductions_employer = []
    for d in ss.deductions:
        entry = {"component": d.salary_component, "amount": flt(d.amount, 2)}
        if d.do_not_include_in_total:
            deductions_employer.append(entry)
        else:
            deductions_employee.append(entry)

    return {
        "company_name": company.company_name,
        "employee_name": emp.employee_name,
        "employee_id": emp.name,
        "designation": emp.designation or "",
        "department": emp.department or "",
        "date_of_joining": str(emp.date_of_joining) if emp.date_of_joining else "",
        "sg_pr_status": emp.sg_pr_status or "",
        "pay_period": f"{formatdate(ss.start_date)} - {formatdate(ss.end_date)}",
        "payment_date": formatdate(ss.posting_date),
        "total_working_days": ss.total_working_days,
        "payment_days": ss.payment_days,
        "earnings": earnings,
        "deductions_employee": deductions_employee,
        "deductions_employer": deductions_employer,
        "gross_pay": flt(ss.gross_pay, 2),
        "total_deduction": flt(ss.total_deduction, 2),
        "net_pay": flt(ss.net_pay, 2),
        "net_pay_words": ss.total_in_words or "",
    }
