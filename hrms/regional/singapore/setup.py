import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def setup_singapore():
    """One-time setup for Singapore payroll compliance."""
    create_sg_custom_fields()
    create_sg_salary_components()
    create_sg_salary_structure()
    frappe.db.commit()
    print("Singapore payroll setup complete!")


def create_sg_custom_fields():
    custom_fields = {
        "Employee": [
            {
                "fieldname": "sg_pr_status",
                "label": "SG Residency Status",
                "fieldtype": "Select",
                "options": "\nSingapore Citizen\nPR - 1st Year\nPR - 2nd Year\nPR - 3rd Year+\nForeigner",
                "insert_after": "date_of_birth",
                "description": "CPF contribution rates depend on residency status",
            },
            {
                "fieldname": "sg_ethnicity",
                "label": "SG Ethnicity (for SHG Fund)",
                "fieldtype": "Select",
                "options": "\nChinese\nMalay\nIndian\nEurasian\nOther",
                "insert_after": "sg_pr_status",
                "description": "Determines CDAC/MBMF/SINDA/ECF contribution",
            },
        ]
    }
    create_custom_fields(custom_fields, update=True)
    print("  Custom fields created on Employee")


def create_sg_salary_components():
    components = [
        {
            "salary_component": "Basic Salary",
            "salary_component_abbr": "BS",
            "type": "Earning",
        },
        {
            "salary_component": "Employee CPF",
            "salary_component_abbr": "ECPF",
            "type": "Deduction",
            "amount_based_on_formula": 1,
                "do_not_include_in_total": nit,
            "formula": "sg_cpf_employee(BS, date_of_birth, sg_pr_status)",
            "depends_on_payment_days": 0,
            "description": "Employee CPF contribution (auto-calculated based on age and residency)",
        },
        {
            "salary_component": "Employer CPF",
            "salary_component_abbr": "ERCPF",
            "type": "Deduction",
            "amount_based_on_formula": 1,
                "do_not_include_in_total": nit,
            "do_not_include_in_total": 1,
            "formula": "sg_cpf_employer(BS, date_of_birth, sg_pr_status)",
            "depends_on_payment_days": 0,
            "description": "Employer CPF contribution (not deducted from employee pay)",
        },
        {
            "salary_component": "SDL",
            "salary_component_abbr": "SDL",
            "type": "Deduction",
            "amount_based_on_formula": 1,
                "do_not_include_in_total": nit,
            "do_not_include_in_total": 1,
            "formula": "sg_sdl(BS)",
            "depends_on_payment_days": 0,
            "description": "Skills Development Levy 0.25% (employer-borne, min $2 max $11.25)",
        },
        {
            "salary_component": "SHG Fund",
            "salary_component_abbr": "SHG",
            "type": "Deduction",
            "amount_based_on_formula": 1,
                "do_not_include_in_total": nit,
            "formula": "sg_shg(BS, sg_ethnicity)",
            "depends_on_payment_days": 0,
            "description": "Self-Help Group: CDAC/MBMF/SINDA/ECF based on ethnicity",
        },
    ]

    for comp in components:
        name = comp["salary_component"]
        if not frappe.db.exists("Salary Component", name):
            doc = frappe.new_doc("Salary Component")
            for key, val in comp.items():
                doc.set(key, val)
            doc.insert(ignore_permissions=True)
            print(f"  Created: {name}")
        else:
            doc = frappe.get_doc("Salary Component", name)
            if comp.get("formula"):
                doc.amount_based_on_formula = 1
                doc.formula = comp["formula"]
                doc.do_not_include_in_total = comp.get("do_not_include_in_total", 0)
                doc.save(ignore_permissions=True)
                print(f"  Updated: {name}")
            else:
                print(f"  Exists: {name}")


def create_sg_salary_structure():
    if frappe.db.exists("Salary Structure", "Singapore Standard"):
        print("  Salary Structure 'Singapore Standard' already exists")
        return

    companies = frappe.get_all("Company", pluck="name", limit=1)
    if not companies:
        print("  WARNING: No company found, skipping salary structure")
        return

    ss = frappe.new_doc("Salary Structure")
    ss.name1 = "Singapore Standard"
    ss.payroll_frequency = "Monthly"
    ss.is_active = "Yes"
    ss.company = companies[0]

    ss.append("earnings", {
        "salary_component": "Basic Salary",
        "abbr": "BS",
        "formula": "base",
        "amount_based_on_formula": 1,
                "do_not_include_in_total": nit,
    })

    for comp_name, abbr, formula, nit in [
        ("Employee CPF", "ECPF", "sg_cpf_employee(BS, date_of_birth, sg_pr_status)", 0),
        ("Employer CPF", "ERCPF", "sg_cpf_employer(BS, date_of_birth, sg_pr_status)", 1),
        ("SDL", "SDL", "sg_sdl(BS)", 1),
        ("Employee CPF", "ECPF", "sg_cpf_employee(BS, date_of_birth, sg_pr_status)", 0),
        ("SHG Fund", "SHG", "sg_shg(BS, sg_ethnicity)", 0),
    ]:
        if frappe.db.exists("Salary Component", comp_name):
            ss.append("deductions", {
                "salary_component": comp_name,
                "abbr": abbr,
                "formula": formula,
                "amount_based_on_formula": 1,
                "do_not_include_in_total": nit,
            })

    ss.insert(ignore_permissions=True)
    ss.submit()
    print(f"  Created Salary Structure: Singapore Standard")
