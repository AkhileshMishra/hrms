# Singapore Payroll Compliance

## Overview
This guide covers Singapore-specific payroll compliance including CPF calculations, SDL, SHG Fund, IR8A tax filing, and MOM-compliant payslip generation.

---

## Singapore Employee Fields Setup

**URL:** `/app/employee`

**Workspace:** HR

### Required SG Fields

| Field | Location | Options | Description |
|-------|----------|---------|-------------|
| SG Residency Status | Employee Form | Singapore Citizen / Singapore PR / Foreigner | Determines CPF applicability |
| SG Ethnicity | Employee Form | Chinese / Malay / Indian / Others | Determines SHG Fund |
| NRIC/FIN | Employee Form | Text | National ID number |
| PR Start Date | Employee Form | Date | For PR graduated rates |
| Date of Birth | Employee Form | Date | For age-based CPF rates |

### How to Set Up SG Employee Fields
1. Click **Sidebar** → **HR**
2. Click **Employee** in shortcuts
3. Open employee record or create new
4. Scroll to **Singapore Details** section
5. Select **SG Residency Status**:
   - Singapore Citizen
   - Singapore PR
   - Foreigner
6. Select **SG Ethnicity**:
   - Chinese
   - Malay
   - Indian
   - Others
7. Enter **NRIC/FIN** number
8. If PR, enter **PR Start Date**
9. Ensure **Date of Birth** is filled (for age-based rates)
10. Click **Save**

---

## CPF Calculation

### CPF Overview

Central Provident Fund (CPF) is mandatory for:
- Singapore Citizens
- Singapore Permanent Residents (PRs)

CPF is NOT applicable for:
- Foreigners (Work Permit, S Pass, Employment Pass holders)

### CPF Rate Tables - Singapore Citizens

#### Citizens: Age 55 and Below

| Monthly Wage | Employee Rate | Employer Rate | Total |
|--------------|---------------|---------------|-------|
| ≤ $50 | 0% | 0% | 0% |
| $50.01 - $500 | 0% | 17% | 17% |
| $500.01 - $750 | 0.6 × (TW - $500) | 17% | Variable |
| > $750 | 20% | 17% | 37% |

#### Citizens: Above 55 to 60

| Monthly Wage | Employee Rate | Employer Rate | Total |
|--------------|---------------|---------------|-------|
| ≤ $50 | 0% | 0% | 0% |
| $50.01 - $500 | 0% | 14.5% | 14.5% |
| $500.01 - $750 | 0.45 × (TW - $500) | 14.5% | Variable |
| > $750 | 15% | 14.5% | 29.5% |

#### Citizens: Above 60 to 65

| Monthly Wage | Employee Rate | Employer Rate | Total |
|--------------|---------------|---------------|-------|
| ≤ $50 | 0% | 0% | 0% |
| $50.01 - $500 | 0% | 11% | 11% |
| $500.01 - $750 | 0.225 × (TW - $500) | 11% | Variable |
| > $750 | 9.5% | 11% | 20.5% |

#### Citizens: Above 65 to 70

| Monthly Wage | Employee Rate | Employer Rate | Total |
|--------------|---------------|---------------|-------|
| ≤ $50 | 0% | 0% | 0% |
| $50.01 - $500 | 0% | 8.5% | 8.5% |
| $500.01 - $750 | 0.15 × (TW - $500) | 8.5% | Variable |
| > $750 | 7% | 8.5% | 15.5% |

#### Citizens: Above 70

| Monthly Wage | Employee Rate | Employer Rate | Total |
|--------------|---------------|---------------|-------|
| ≤ $50 | 0% | 0% | 0% |
| $50.01 - $500 | 0% | 7.5% | 7.5% |
| $500.01 - $750 | 0.075 × (TW - $500) | 7.5% | Variable |
| > $750 | 5% | 7.5% | 12.5% |

### CPF Rate Tables - Permanent Residents

#### PR 1st Year (Graduated Rates)

| Age | Employee Rate | Employer Rate | Total |
|-----|---------------|---------------|-------|
| ≤ 55 | 5% | 4% | 9% |
| 55-60 | 5% | 4% | 9% |
| 60-65 | 5% | 3.5% | 8.5% |
| 65-70 | 5% | 3% | 8% |
| > 70 | 5% | 3% | 8% |

#### PR 2nd Year (Graduated Rates)

| Age | Employee Rate | Employer Rate | Total |
|-----|---------------|---------------|-------|
| ≤ 55 | 15% | 9% | 24% |
| 55-60 | 12.5% | 6% | 18.5% |
| 60-65 | 7.5% | 3.5% | 11% |
| 65-70 | 5% | 3% | 8% |
| > 70 | 5% | 3% | 8% |

#### PR 3rd Year and Beyond (Full Rates)

Same as Singapore Citizens (see tables above)

### CPF Wage Ceiling

| Type | Amount | Description |
|------|--------|-------------|
| Ordinary Wage Ceiling | $6,800/month | Max OW for CPF |
| Additional Wage Ceiling | $102,000 - OW | Annual AW ceiling |

### How to Create CPF Salary Components

#### CPF Employee Contribution
1. Click **Sidebar** → **Payroll**
2. Click **Salary Component** in shortcuts
3. Click **+ Add Salary Component**
4. Enter **Name**: "CPF Employee"
5. Enter **Abbr**: "CPFE"
6. Select **Type**: "Deduction"
7. Check **Amount Based On Formula**
8. Enter **Formula** (example for citizen ≤55):
   ```
   base * 0.20 if base > 750 else (0.6 * (base - 500) if base > 500 else 0)
   ```
9. Enter **Condition**:
   ```
   sg_residency_status == "Singapore Citizen" and employee_age <= 55
   ```
10. Click **Save**

#### CPF Employer Contribution
1. Click **+ Add Salary Component**
2. Enter **Name**: "CPF Employer"
3. Enter **Abbr**: "CPFER"
4. Select **Type**: "Deduction"
5. Check **Do Not Include In Total** (employer cost)
6. Check **Amount Based On Formula**
7. Enter **Formula**:
   ```
   base * 0.17 if base > 50 else 0
   ```
8. Enter **Condition**:
   ```
   sg_residency_status == "Singapore Citizen" and employee_age <= 55
   ```
9. Click **Save**

---

## SDL (Skills Development Levy)

### SDL Overview

| Item | Value |
|------|-------|
| Rate | 0.25% of monthly wages |
| Minimum | $2 per employee |
| Maximum | $11.25 per employee |
| Applicable To | All employees (including foreigners) |

### SDL Calculation

```
SDL = MAX(MIN(Monthly Wage × 0.0025, 11.25), 2)
```

| Monthly Wage | SDL Amount |
|--------------|------------|
| $800 | $2.00 (minimum) |
| $1,000 | $2.50 |
| $2,000 | $5.00 |
| $4,500 | $11.25 (maximum) |
| $10,000 | $11.25 (maximum) |

### How to Create SDL Salary Component
1. Click **Sidebar** → **Payroll**
2. Click **Salary Component** in shortcuts
3. Click **+ Add Salary Component**
4. Enter **Name**: "SDL"
5. Enter **Abbr**: "SDL"
6. Select **Type**: "Deduction"
7. Check **Do Not Include In Total** (employer cost)
8. Check **Amount Based On Formula**
9. Enter **Formula**:
   ```
   max(min(base * 0.0025, 11.25), 2)
   ```
10. Click **Save**

---

## SHG Fund (Self-Help Group)

### SHG Fund Overview

SHG Fund contributions are based on employee ethnicity:

| Ethnicity | Fund | Monthly Contribution |
|-----------|------|---------------------|
| Chinese | CDAC (Chinese Development Assistance Council) | $0.50 - $1.00 |
| Malay | MBMF (Mosque Building and Mendaki Fund) | $1.50 - $5.00 |
| Indian | SINDA (Singapore Indian Development Association) | $0.50 - $3.00 |
| Others | ECF (Eurasian Community Fund) | $0.50 - $2.00 |

### CDAC Contribution Rates (Chinese)

| Monthly Wage | Contribution |
|--------------|--------------|
| $0 - $500 | $0 |
| $501 - $1,000 | $0.50 |
| $1,001 - $2,000 | $1.00 |
| > $2,000 | $1.00 |

### MBMF Contribution Rates (Malay)

| Monthly Wage | Contribution |
|--------------|--------------|
| $0 - $1,000 | $0 |
| $1,001 - $2,000 | $1.50 |
| $2,001 - $3,000 | $2.50 |
| $3,001 - $4,000 | $3.50 |
| $4,001 - $6,000 | $4.50 |
| > $6,000 | $5.00 |

### SINDA Contribution Rates (Indian)

| Monthly Wage | Contribution |
|--------------|--------------|
| $0 - $1,000 | $0 |
| $1,001 - $1,500 | $0.50 |
| $1,501 - $2,500 | $1.00 |
| $2,501 - $5,000 | $2.00 |
| > $5,000 | $3.00 |

### ECF Contribution Rates (Others)

| Monthly Wage | Contribution |
|--------------|--------------|
| $0 - $1,000 | $0 |
| $1,001 - $2,500 | $0.50 |
| $2,501 - $5,000 | $1.00 |
| > $5,000 | $2.00 |

### How to Create SHG Fund Components

#### CDAC Component (Chinese)
1. Click **Sidebar** → **Payroll**
2. Click **Salary Component** → **+ Add Salary Component**
3. Enter **Name**: "CDAC"
4. Enter **Abbr**: "CDAC"
5. Select **Type**: "Deduction"
6. Check **Amount Based On Formula**
7. Enter **Formula**:
   ```
   1.00 if base > 1000 else (0.50 if base > 500 else 0)
   ```
8. Enter **Condition**:
   ```
   sg_ethnicity == "Chinese"
   ```
9. Click **Save**

Repeat for MBMF, SINDA, and ECF with appropriate formulas and conditions.

---

## CPF e-Submission File Generation

### Overview
CPF e-Submission allows electronic submission of CPF contributions to CPF Board.

### File Format Requirements

| Field | Format | Description |
|-------|--------|-------------|
| Employer CPF Account No | 10 digits | Company CPF account |
| Employee NRIC/FIN | 9 characters | Employee ID |
| Employee Name | Text | Full name |
| Ordinary Wages | Decimal | Monthly OW |
| Additional Wages | Decimal | Bonus, etc. |
| CPF Employee | Decimal | Employee contribution |
| CPF Employer | Decimal | Employer contribution |

### How to Generate CPF e-Submission File
1. Click **Sidebar** → **Payroll**
2. Click **CPF e-Submission** in Reports (or custom report)
3. Select **Company**
4. Select **Payroll Period** (month)
5. Click **Generate**
6. Review data
7. Click **Export** → select CPF format
8. Download file
9. Upload to CPF Board portal

---

## IR8A Year-End Tax Filing

### IR8A Overview
IR8A is the annual tax form submitted to IRAS (Inland Revenue Authority of Singapore) for each employee.

### IR8A Fields

| Field | Description |
|-------|-------------|
| Employee Name | Full name |
| NRIC/FIN | ID number |
| Gross Salary | Total earnings |
| Bonus | Annual bonus |
| Director's Fees | If applicable |
| CPF Contributions | Employee CPF |
| Allowances | Transport, etc. |
| Benefits in Kind | Non-cash benefits |

### How to Generate IR8A Report
1. Click **Sidebar** → **Payroll**
2. Click **IR8A Report** in Reports
3. Select **Company**
4. Select **Year** (e.g., 2024)
5. Click **Generate**
6. Review employee tax data
7. Click **Export** → select IRAS format
8. Download file
9. Submit via IRAS myTax Portal

---

## GIRO Bank Payment

### GIRO Overview
GIRO (General Interbank Recurring Order) enables automatic bank transfers for salary payments.

### GIRO File Format

| Field | Description |
|-------|-------------|
| Bank Code | 3-digit bank code |
| Branch Code | 3-digit branch code |
| Account Number | Employee account |
| Account Name | Employee name |
| Amount | Net pay |
| Reference | Salary slip reference |

### How to Generate GIRO Payment File
1. Process payroll (see Payroll Entry workflow)
2. After submitting salary slips, click **Make Bank Entry**
3. Select **Payment Account** (company bank)
4. Click **Create**
5. Go to **Sidebar** → **Payroll**
6. Click **Bank Remittance** report
7. Select **From Date** and **To Date**
8. Select **Company**
9. Click **Export** → select GIRO format
10. Download file
11. Upload to bank portal

---

## MOM-Compliant Payslip

### MOM Payslip Requirements

Ministry of Manpower requires payslips to include:

| Required Item | Description |
|---------------|-------------|
| Full Name | Employee name |
| Date of Payment | Pay date |
| Basic Salary | Base pay |
| Start/End of Salary Period | Pay period |
| Allowances | Itemized |
| Deductions | Itemized (CPF, etc.) |
| Overtime Hours & Pay | If applicable |
| Net Salary | Take-home pay |

### How to Configure MOM-Compliant Payslip
1. Press `Ctrl + K` → type "Print Format"
2. Click **+ Add Print Format**
3. Enter **Name**: "MOM Payslip"
4. Select **Doc Type**: "Salary Slip"
5. Check **Standard**: No (custom)
6. Design format to include all MOM requirements:
   - Employee name and ID
   - Pay period dates
   - Itemized earnings
   - Itemized deductions
   - Overtime details
   - Net pay
7. Click **Save**

### How to Print MOM-Compliant Payslip
1. Open salary slip
2. Click **Menu** (⋮) → **Print**
3. Select **Print Format**: "MOM Payslip"
4. Click **Print** or **PDF**

---

## Complete SG Payroll Setup Walkthrough

### Step-by-Step Setup

#### Step 1: Configure Employee SG Fields
1. For each employee, set:
   - SG Residency Status
   - SG Ethnicity
   - NRIC/FIN
   - Date of Birth
   - PR Start Date (if applicable)

#### Step 2: Create CPF Salary Components
1. Create "CPF Employee" component (deduction)
2. Create "CPF Employer" component (deduction, not in total)
3. Set formulas based on residency and age
4. Create components for each age bracket if needed

#### Step 3: Create SDL Component
1. Create "SDL" component (deduction, not in total)
2. Formula: `max(min(base * 0.0025, 11.25), 2)`

#### Step 4: Create SHG Fund Components
1. Create CDAC component (condition: Chinese)
2. Create MBMF component (condition: Malay)
3. Create SINDA component (condition: Indian)
4. Create ECF component (condition: Others)

#### Step 5: Create Salary Structure
1. Create new salary structure
2. Add earnings: Basic Salary, Allowances
3. Add deductions: CPF Employee, CDAC/MBMF/SINDA/ECF
4. Add employer costs: CPF Employer, SDL

#### Step 6: Assign Salary Structure
1. Assign structure to employees
2. Set base salary for each

#### Step 7: Configure Payslip Print Format
1. Create MOM-compliant print format
2. Set as default for salary slips

#### Step 8: Process Monthly Payroll
1. Create Payroll Entry
2. Get Employees
3. Create Salary Slips
4. Review CPF calculations
5. Submit Salary Slips
6. Generate GIRO file
7. Generate CPF e-Submission file

#### Step 9: Year-End Filing
1. Generate IR8A report
2. Submit to IRAS

---

## Quick Reference

### Key SG Compliance URLs

| Document/Report | URL |
|-----------------|-----|
| Employee | `/app/employee` |
| Salary Component | `/app/salary-component` |
| Salary Structure | `/app/salary-structure` |
| Payroll Entry | `/app/payroll-entry` |
| Salary Slip | `/app/salary-slip` |
| Bank Remittance | `/app/query-report/Bank Remittance` |

### CPF Quick Reference

| Category | Employee | Employer | Total |
|----------|----------|----------|-------|
| Citizen ≤55 | 20% | 17% | 37% |
| Citizen 55-60 | 15% | 14.5% | 29.5% |
| Citizen 60-65 | 9.5% | 11% | 20.5% |
| PR 1st Year | 5% | 4% | 9% |
| PR 2nd Year | 15% | 9% | 24% |
| PR 3rd Year+ | Full rates | Full rates | Full rates |

### SG Payroll Checklist
- [ ] Employee SG fields configured
- [ ] CPF components created (all age brackets)
- [ ] SDL component created
- [ ] SHG Fund components created (all ethnicities)
- [ ] Salary structure with SG components
- [ ] MOM-compliant payslip format
- [ ] CPF e-Submission process tested
- [ ] GIRO payment process tested
- [ ] IR8A report configured
