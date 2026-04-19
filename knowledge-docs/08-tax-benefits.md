# Tax & Benefits Management

## Overview
This guide covers income tax configuration, employee tax declarations, benefit applications, gratuity management, and related reports.

---

## Income Tax Slab

**URL:** `/app/income-tax-slab`

**Workspace:** Tax & Benefits

Income Tax Slab defines tax brackets for calculating employee income tax deductions.

### Income Tax Slab Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Name | Yes | Data | Slab identifier |
| Company | Yes | Link | Applicable company |
| Currency | Yes | Link | Tax currency |
| Effective From | Yes | Date | Start date |
| Disabled | No | Check | Deactivate slab |
| Taxable Salary Slabs | Yes | Table | Tax brackets |

### Taxable Salary Slabs Table

| Field | Required | Description |
|-------|----------|-------------|
| From Amount | Yes | Bracket start |
| To Amount | Yes | Bracket end |
| Percent Deduction | Cond | Tax percentage |
| Fixed Amount | Cond | Fixed tax amount |
| Condition | No | Additional condition |

### How to Create Income Tax Slab
1. Click **Sidebar** → **Tax & Benefits**
2. Click **Income Tax Slab** in shortcuts
3. Click **+ Add Income Tax Slab**
4. Enter **Name** (e.g., "Singapore Tax 2024")
5. Select **Company**
6. Select **Currency**
7. Select **Effective From** date
8. In **Taxable Salary Slabs** table:
   - Click **Add Row**
   - Enter **From Amount** (e.g., 0)
   - Enter **To Amount** (e.g., 20000)
   - Enter **Percent Deduction** (e.g., 0)
   - Repeat for each tax bracket
9. Click **Save**

### Sample Singapore Tax Brackets (Resident)

| From Amount | To Amount | Tax Rate |
|-------------|-----------|----------|
| $0 | $20,000 | 0% |
| $20,001 | $30,000 | 2% |
| $30,001 | $40,000 | 3.5% |
| $40,001 | $80,000 | 7% |
| $80,001 | $120,000 | 11.5% |
| $120,001 | $160,000 | 15% |
| $160,001 | $200,000 | 18% |
| $200,001 | $240,000 | 19% |
| $240,001 | $280,000 | 19.5% |
| $280,001 | $320,000 | 20% |
| $320,001 | $500,000 | 22% |
| $500,001 | $1,000,000 | 23% |
| > $1,000,000 | - | 24% |

### How to Assign Tax Slab to Employee
1. Open **Salary Structure Assignment** for employee
2. Select **Income Tax Slab** field
3. Choose the appropriate tax slab
4. Click **Save**

---

## Employee Tax Exemption Declaration

**URL:** `/app/employee-tax-exemption-declaration`

**Workspace:** Tax & Benefits

Employees declare tax-saving investments at the start of the year for TDS calculation.

### Declaration Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Employee reference |
| Company | Yes | Link | Company |
| Payroll Period | Yes | Link | Tax year |
| Currency | Yes | Link | Currency |
| Declarations | Yes | Table | Exemption items |
| Total Declared Amount | Auto | Currency | Sum of declarations |
| Total Exemption Amount | Auto | Currency | Eligible exemption |

### Declarations Table

| Field | Required | Description |
|-------|----------|-------------|
| Exemption Sub Category | Yes | Type of exemption |
| Exemption Category | Auto | Parent category |
| Maximum Exempted Amount | Auto | Category limit |
| Declared Amount | Yes | Amount declared |

### How to Submit Tax Exemption Declaration (Employee)
1. Click **Sidebar** → **Tax & Benefits**
2. Click **Employee Tax Exemption Declaration** in shortcuts
3. Click **+ Add Employee Tax Exemption Declaration**
4. **Employee** auto-fills with your name
5. Select **Company**
6. Select **Payroll Period** (e.g., "FY 2024")
7. In **Declarations** table:
   - Click **Add Row**
   - Select **Exemption Sub Category** (e.g., "Life Insurance Premium")
   - Enter **Declared Amount**
   - Repeat for each investment
8. Review **Total Declared Amount**
9. Click **Save**
10. Click **Submit**

### Common Exemption Categories

| Category | Sub-Categories | Max Limit |
|----------|----------------|-----------|
| Section 80C | Life Insurance, PPF, ELSS, NSC | Varies |
| Section 80D | Health Insurance Premium | Varies |
| HRA | House Rent Allowance | Calculated |
| LTA | Leave Travel Allowance | Actual |

---

## Employee Tax Exemption Proof Submission

**URL:** `/app/employee-tax-exemption-proof-submission`

**Workspace:** Tax & Benefits

Employees submit proof of declared investments for final tax calculation.

### Proof Submission Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Employee reference |
| Company | Yes | Link | Company |
| Payroll Period | Yes | Link | Tax year |
| Submission Date | Yes | Date | Date of submission |
| Tax Exemption Proofs | Yes | Table | Proof items |
| Total Actual Amount | Auto | Currency | Sum of actual amounts |

### Tax Exemption Proofs Table

| Field | Required | Description |
|-------|----------|-------------|
| Exemption Sub Category | Yes | Type of exemption |
| Exemption Category | Auto | Parent category |
| Maximum Exempted Amount | Auto | Category limit |
| Type of Proof | Yes | Document type |
| Actual Amount | Yes | Actual investment |
| Attach Proof | No | Upload document |

### How to Submit Tax Exemption Proof (Employee)
1. Click **Sidebar** → **Tax & Benefits**
2. Click **Employee Tax Exemption Proof Submission** in shortcuts
3. Click **+ Add Employee Tax Exemption Proof Submission**
4. **Employee** auto-fills
5. Select **Company**
6. Select **Payroll Period**
7. Select **Submission Date**
8. In **Tax Exemption Proofs** table:
   - Click **Add Row**
   - Select **Exemption Sub Category**
   - Select **Type of Proof** (Receipt/Certificate/etc.)
   - Enter **Actual Amount**
   - Click **Attach Proof** → upload document
   - Repeat for each proof
9. Click **Save**
10. Click **Submit**

### How to Verify Tax Proofs (HR)
1. Click **Sidebar** → **Tax & Benefits**
2. Click **Employee Tax Exemption Proof Submission**
3. Filter by **Status** → "Submitted"
4. Open submission
5. Review each proof:
   - Check attached documents
   - Verify amounts
6. Click **Approve** or **Reject**

---

## Employee Benefit Application

**URL:** `/app/employee-benefit-application`

**Workspace:** Tax & Benefits

Employees apply for flexible benefits from their salary package.

### Benefit Application Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Employee reference |
| Company | Yes | Link | Company |
| Payroll Period | Yes | Link | Benefit period |
| Date | Yes | Date | Application date |
| Employee Benefits | Yes | Table | Benefit items |
| Total Amount | Auto | Currency | Sum of benefits |
| Remaining Benefits | Auto | Currency | Available balance |

### Employee Benefits Table

| Field | Required | Description |
|-------|----------|-------------|
| Earning Component | Yes | Benefit component |
| Max Benefit Amount | Auto | Maximum allowed |
| Amount | Yes | Requested amount |
| Pay Against Benefit Claim | No | Claim-based payment |

### How to Apply for Benefits (Employee)
1. Click **Sidebar** → **Tax & Benefits**
2. Click **Employee Benefit Application** in shortcuts
3. Click **+ Add Employee Benefit Application**
4. **Employee** auto-fills
5. Select **Company**
6. Select **Payroll Period**
7. Select **Date**
8. In **Employee Benefits** table:
   - Click **Add Row**
   - Select **Earning Component** (e.g., "Meal Allowance")
   - Enter **Amount**
   - Check **Pay Against Benefit Claim** if claim-based
   - Repeat for each benefit
9. Review **Total Amount** and **Remaining Benefits**
10. Click **Save**
11. Click **Submit**

---

## Employee Benefit Claim

**URL:** `/app/employee-benefit-claim`

**Workspace:** Tax & Benefits

Employees claim reimbursement for benefits marked as claim-based.

### Benefit Claim Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Employee reference |
| Company | Yes | Link | Company |
| Claim Date | Yes | Date | Date of claim |
| Currency | Yes | Link | Claim currency |
| Employee Benefit Claim | Yes | Table | Claim items |
| Total Claimed Amount | Auto | Currency | Sum of claims |

### Employee Benefit Claim Table

| Field | Required | Description |
|-------|----------|-------------|
| Earning Component | Yes | Benefit component |
| Max Amount Eligible | Auto | Available balance |
| Claimed Amount | Yes | Amount claimed |
| Claim Proof | No | Upload receipt |

### How to Submit Benefit Claim (Employee)
1. Click **Sidebar** → **Tax & Benefits**
2. Click **Employee Benefit Claim** in shortcuts
3. Click **+ Add Employee Benefit Claim**
4. **Employee** auto-fills
5. Select **Company**
6. Select **Claim Date**
7. In **Employee Benefit Claim** table:
   - Click **Add Row**
   - Select **Earning Component**
   - Enter **Claimed Amount**
   - Click **Claim Proof** → upload receipt
   - Repeat for each claim
8. Click **Save**
9. Click **Submit**

### How to Approve Benefit Claim (HR)
1. Click **Sidebar** → **Tax & Benefits**
2. Click **Employee Benefit Claim**
3. Filter by **Status** → "Submitted"
4. Open claim
5. Review:
   - Claimed amounts
   - Attached proofs
6. Click **Approve** or **Reject**

---

## Gratuity

**URL:** `/app/gratuity`

**Workspace:** Tax & Benefits

Gratuity is a lump-sum payment to employees upon separation based on service tenure.

### Gratuity Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Employee reference |
| Company | Yes | Link | Company |
| Gratuity Rule | Yes | Link | Calculation rule |
| Payroll Date | Yes | Date | Payment date |
| Pay Via Salary Slip | No | Check | Include in payslip |
| Amount | Auto | Currency | Calculated gratuity |
| Current Work Experience | Auto | Float | Years of service |

### How to Process Gratuity
1. Click **Sidebar** → **Tax & Benefits**
2. Click **Gratuity** in shortcuts
3. Click **+ Add Gratuity**
4. Select **Employee**
5. Select **Company**
6. Select **Gratuity Rule**
7. Select **Payroll Date**
8. Check **Pay Via Salary Slip** if including in payslip
9. **Amount** auto-calculates based on rule
10. Review **Current Work Experience**
11. Click **Save**
12. Click **Submit**

---

## Gratuity Rule

**URL:** `/app/gratuity-rule`

**Workspace:** Tax & Benefits

Gratuity Rule defines how gratuity is calculated based on service tenure.

### Gratuity Rule Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Name | Yes | Data | Rule name |
| Company | Yes | Link | Applicable company |
| Work Experience Calculation Method | Yes | Select | Current/Total |
| Gratuity Rule Slabs | Yes | Table | Calculation slabs |

### Gratuity Rule Slabs Table

| Field | Required | Description |
|-------|----------|-------------|
| From Year | Yes | Service years start |
| To Year | Yes | Service years end |
| Fraction of Applicable Earnings | Yes | Multiplier |

### How to Create Gratuity Rule
1. Click **Sidebar** → **Tax & Benefits**
2. Click **Gratuity Rule** in shortcuts
3. Click **+ Add Gratuity Rule**
4. Enter **Name** (e.g., "Standard Gratuity Rule")
5. Select **Company**
6. Select **Work Experience Calculation Method**
7. In **Gratuity Rule Slabs** table:
   - Click **Add Row**
   - Enter **From Year** (e.g., 0)
   - Enter **To Year** (e.g., 5)
   - Enter **Fraction of Applicable Earnings** (e.g., 0.5)
   - Add more slabs for different tenure ranges
8. Click **Save**

### Sample Gratuity Rule

| From Year | To Year | Fraction |
|-----------|---------|----------|
| 0 | 5 | 0.5 (15 days per year) |
| 5 | 10 | 1.0 (1 month per year) |
| 10 | 999 | 1.5 (1.5 months per year) |

---

## Tax & Benefits Reports

**Workspace:** Tax & Benefits

### Available Reports

| Report | URL | Description |
|--------|-----|-------------|
| Employee Tax Exemption Summary | `/app/query-report/Employee Tax Exemption Summary` | Declaration vs proof summary |
| Income Tax Computation | `/app/query-report/Income Tax Computation` | Tax calculation details |
| Gratuity Report | `/app/query-report/Gratuity Report` | Gratuity liability |

### How to View Employee Tax Exemption Summary
1. Click **Sidebar** → **Tax & Benefits**
2. Click **Employee Tax Exemption Summary** in Reports
3. Select **Company**
4. Select **Payroll Period**
5. View:
   - Declared amounts
   - Submitted proofs
   - Variance

### How to View Income Tax Computation
1. Click **Sidebar** → **Tax & Benefits**
2. Click **Income Tax Computation** in Reports
3. Select **Employee**
4. Select **Payroll Period**
5. View detailed tax calculation:
   - Gross income
   - Exemptions
   - Taxable income
   - Tax liability

---

## Quick Reference

### Tax & Benefits Setup Checklist
- [ ] Create Income Tax Slabs
- [ ] Create Exemption Categories (if needed)
- [ ] Create Gratuity Rules
- [ ] Configure benefit components
- [ ] Assign tax slabs to employees

### Key URLs

| Document | URL |
|----------|-----|
| Income Tax Slab | `/app/income-tax-slab` |
| Employee Tax Exemption Declaration | `/app/employee-tax-exemption-declaration` |
| Employee Tax Exemption Proof Submission | `/app/employee-tax-exemption-proof-submission` |
| Employee Benefit Application | `/app/employee-benefit-application` |
| Employee Benefit Claim | `/app/employee-benefit-claim` |
| Gratuity | `/app/gratuity` |
| Gratuity Rule | `/app/gratuity-rule` |

### Tax Declaration Timeline

| Period | Action |
|--------|--------|
| Start of Year | Submit Tax Exemption Declaration |
| Throughout Year | TDS calculated based on declaration |
| End of Year | Submit Tax Exemption Proof |
| After Verification | Final tax adjustment |

### Required Roles
| Action | Required Role |
|--------|---------------|
| Submit declaration | Employee |
| Submit proof | Employee |
| Verify proofs | HR User, HR Manager |
| Create tax slabs | HR Manager |
| Process gratuity | HR Manager |
