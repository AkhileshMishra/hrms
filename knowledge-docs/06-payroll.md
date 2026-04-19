# Payroll Management

## Overview
This guide covers complete payroll processing including salary components, structures, assignments, payroll entry workflow, and reports.

---

## Salary Component

**URL:** `/app/salary-component`

**Workspace:** Payroll

Salary Components are the building blocks of salary structures (earnings and deductions).

### Salary Component Fields

| Section | Field | Required | Description |
|---------|-------|----------|-------------|
| **Basic** | Name | Yes | Component name |
| | Abbr | Yes | Short code |
| | Type | Yes | Earning/Deduction |
| | Description | No | Component description |
| **Properties** | Is Payable | No | Include in net pay |
| | Depends On Payment Days | No | Prorate by attendance |
| | Is Tax Applicable | No | Subject to tax |
| | Is Flexible Benefit | No | Flexible benefit component |
| | Variable Based On Taxable Salary | No | Tax-based calculation |
| | Do Not Include In Total | No | Exclude from totals |
| | Disabled | No | Deactivate component |
| **Accounts** | Accounts | No | GL account mapping |
| **Condition & Formula** | Condition | No | When to apply |
| | Amount Based On Formula | No | Use formula |
| | Formula | Cond | Calculation formula |
| | Amount | Cond | Fixed amount |
| | Statistical Component | No | For calculation only |

### Formula Variables

| Variable | Description |
|----------|-------------|
| `base` | Base salary |
| `gross_pay` | Total earnings |
| `H` | Total working hours |
| `D` | Payment days |
| `B` | Basic salary component |
| `custom_field` | Any custom employee field |

### How to Create a Salary Component (Earning)
1. Click **Sidebar** → **Payroll**
2. Click **Salary Component** in shortcuts
3. Click **+ Add Salary Component**
4. Enter **Name** (e.g., "Basic Salary")
5. Enter **Abbr** (e.g., "BS")
6. Select **Type** → "Earning"
7. Check **Is Payable**
8. Check **Depends On Payment Days** (for prorated)
9. Check **Is Tax Applicable** (if taxable)
10. Click **Save**

### How to Create a Salary Component with Formula
1. Follow steps 1-6 above
2. Check **Amount Based On Formula**
3. Enter **Formula**:
   - Example: `base * 0.1` (10% of base)
   - Example: `B * 0.5` (50% of Basic)
4. Optionally enter **Condition**:
   - Example: `base > 5000`
5. Click **Save**

### Common Salary Components

| Component | Type | Formula | Description |
|-----------|------|---------|-------------|
| Basic Salary | Earning | - | Base pay |
| HRA | Earning | `B * 0.4` | House Rent Allowance |
| Transport Allowance | Earning | Fixed | Travel allowance |
| Overtime | Earning | `(B/D/8) * OT_hours * 1.5` | OT pay |
| CPF Employee | Deduction | Formula | Employee CPF |
| CPF Employer | Deduction | Formula | Employer CPF |
| Income Tax | Deduction | Formula | Tax deduction |

---

## Salary Structure

**URL:** `/app/salary-structure`

**Workspace:** Payroll

Salary Structure defines the complete salary breakdown for a category of employees.

### Salary Structure Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Name | Yes | Data | Structure name |
| Company | Yes | Link | Applicable company |
| Is Active | Yes | Check | Active status |
| Payroll Frequency | Yes | Select | Monthly/Weekly/etc. |
| Letter Head | No | Link | For payslip printing |
| Earnings | Yes | Table | Earning components |
| Deductions | Yes | Table | Deduction components |

### Earnings/Deductions Table Fields

| Field | Required | Description |
|-------|----------|-------------|
| Salary Component | Yes | Component reference |
| Abbr | Auto | Auto-filled |
| Formula | Cond | Calculation formula |
| Amount | Cond | Fixed amount |
| Condition | No | When to apply |
| Amount Based On Formula | No | Use formula |
| Do Not Include In Total | No | Exclude from totals |

### How to Create a Salary Structure
1. Click **Sidebar** → **Payroll**
2. Click **Salary Structure** in shortcuts
3. Click **+ Add Salary Structure**
4. Enter **Name** (e.g., "Standard Employee Structure")
5. Select **Company**
6. Check **Is Active**
7. Select **Payroll Frequency** (e.g., Monthly)

   **Add Earnings:**
8. In **Earnings** table, click **Add Row**
9. Select **Salary Component** (e.g., "Basic Salary")
10. Enter **Amount** or check **Amount Based On Formula** and enter **Formula**
11. Repeat for all earning components

    **Add Deductions:**
12. In **Deductions** table, click **Add Row**
13. Select **Salary Component** (e.g., "CPF Employee")
14. Enter **Amount** or **Formula**
15. Repeat for all deduction components
16. Click **Save**

---

## Salary Structure Assignment

**URL:** `/app/salary-structure-assignment`

**Workspace:** Payroll

Salary Structure Assignment links a salary structure to an employee with their base salary.

### Assignment Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Employee reference |
| Salary Structure | Yes | Link | Structure to assign |
| From Date | Yes | Date | Effective date |
| Company | Yes | Link | Company |
| Base | Yes | Currency | Base salary amount |
| Variable | No | Currency | Variable pay |
| Income Tax Slab | No | Link | Tax slab reference |

### How to Assign Salary Structure (Individual)
1. Click **Sidebar** → **Payroll**
2. Click **Salary Structure Assignment** in shortcuts
3. Click **+ Add Salary Structure Assignment**
4. Select **Employee**
5. Select **Salary Structure**
6. Select **From Date** (effective date)
7. Select **Company**
8. Enter **Base** salary amount
9. Enter **Variable** pay (optional)
10. Select **Income Tax Slab** (optional)
11. Click **Save**
12. Click **Submit**

### How to Bulk Assign Salary Structure
1. Click **Sidebar** → **Payroll**
2. Click **Salary Structure** in shortcuts
3. Open the salary structure
4. Click **Assign Salary Structure** button
5. Select **Company**
6. Select **From Date**
7. Filter by:
   - Department
   - Designation
   - Employee Grade
   - Payroll Payable Account
8. Enter **Base** amount (or leave for individual entry)
9. Click **Get Employees**
10. Review employee list
11. Enter **Base** for each employee (if not set)
12. Click **Assign**

---

## Payroll Entry (Full Workflow)

**URL:** `/app/payroll-entry`

**Workspace:** Payroll

Payroll Entry is the main document for processing monthly payroll.

### Payroll Entry Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Company | Yes | Link | Company |
| Posting Date | Yes | Date | Payroll date |
| Payroll Frequency | Yes | Select | Monthly/Weekly |
| Start Date | Yes | Date | Period start |
| End Date | Yes | Date | Period end |
| Currency | Yes | Link | Payment currency |
| Exchange Rate | Yes | Float | Currency rate |
| Department | No | Link | Filter by department |
| Branch | No | Link | Filter by branch |
| Designation | No | Link | Filter by designation |
| Employees | Auto | Table | Selected employees |

### Complete Payroll Workflow

#### Step 1: Create Payroll Entry
1. Click **Sidebar** → **Payroll**
2. Click **Payroll Entry** in shortcuts
3. Click **+ Add Payroll Entry**
4. Select **Company**
5. Select **Posting Date**
6. Select **Payroll Frequency** (Monthly)
7. Select **Start Date** (e.g., 2024-01-01)
8. Select **End Date** (e.g., 2024-01-31)
9. Optionally filter by **Department**, **Branch**, **Designation**
10. Click **Save**

#### Step 2: Get Employees
1. Click **Get Employees** button
2. System fetches employees with:
   - Active salary structure assignment
   - Matching filters (department, branch, etc.)
3. Review **Employees** table
4. Remove any employees if needed (uncheck or delete row)
5. Click **Save**

#### Step 3: Create Salary Slips
1. Click **Create Salary Slips** button
2. System creates draft salary slips for all employees
3. Wait for process to complete
4. Status shows "Salary Slips Created"
5. Click **View Salary Slips** to review

#### Step 4: Review Salary Slips
1. Click **View Salary Slips** link
2. Opens list of created salary slips
3. Click any slip to review details
4. Verify:
   - Earnings calculated correctly
   - Deductions applied
   - Net pay is accurate
5. Make corrections if needed

#### Step 5: Submit Salary Slips
1. Return to Payroll Entry
2. Click **Submit Salary Slips** button
3. All salary slips are submitted
4. Status shows "Salary Slips Submitted"

#### Step 6: Create Bank Entry (Payment)
1. Click **Make Bank Entry** button
2. Select **Payment Account** (bank account)
3. Review payment details
4. Click **Create**
5. Journal Entry is created for salary payment
6. Submit the Journal Entry to complete

### Payroll Entry Status Flow
```
Draft → Salary Slips Created → Salary Slips Submitted → Bank Entry Created
```

---

## Salary Slip

**URL:** `/app/salary-slip`

**Workspace:** Payroll

Salary Slip is the individual payslip for each employee.

### Salary Slip Fields

| Section | Field | Description |
|---------|-------|-------------|
| **Employee** | Employee | Employee reference |
| | Employee Name | Auto-filled |
| | Department | Auto-filled |
| | Designation | Auto-filled |
| **Payroll** | Posting Date | Slip date |
| | Start Date | Period start |
| | End Date | Period end |
| | Salary Structure | Applied structure |
| **Earnings** | Earnings | Table of earnings |
| **Deductions** | Deductions | Table of deductions |
| **Totals** | Gross Pay | Total earnings |
| | Total Deduction | Total deductions |
| | Net Pay | Take-home pay |
| **Payment** | Mode of Payment | Payment method |
| | Bank Account No | Employee bank |

### How to Create Individual Salary Slip
1. Click **Sidebar** → **Payroll**
2. Click **Salary Slip** in shortcuts
3. Click **+ Add Salary Slip**
4. Select **Employee**
5. Select **Posting Date**
6. Select **Start Date** and **End Date**
7. Click **Get Salary Structure**
8. Earnings and Deductions auto-populate
9. Review and adjust if needed
10. Click **Save**
11. Click **Submit**

### How to Print Salary Slip
1. Open the salary slip
2. Click **Menu** (⋮) → **Print**
3. Select **Print Format**
4. Click **Print** or **PDF**

---

## Additional Salary

**URL:** `/app/additional-salary`

**Workspace:** Payroll

Additional Salary adds one-time or recurring payments/deductions outside the regular structure.

### Additional Salary Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Employee reference |
| Salary Component | Yes | Link | Component to add |
| Company | Yes | Link | Company |
| Payroll Date | Yes | Date | When to apply |
| Amount | Yes | Currency | Amount to add |
| Overwrite Salary Structure Amount | No | Check | Replace structure amount |
| Is Recurring | No | Check | Repeat monthly |
| From Date | Cond | Date | Recurring start |
| To Date | Cond | Date | Recurring end |

### How to Add Additional Salary
1. Click **Sidebar** → **Payroll**
2. Click **Additional Salary** in shortcuts
3. Click **+ Add Additional Salary**
4. Select **Employee**
5. Select **Salary Component** (e.g., "Bonus")
6. Select **Company**
7. Select **Payroll Date** (month to apply)
8. Enter **Amount**
9. Check **Is Recurring** if monthly
   - If recurring, set **From Date** and **To Date**
10. Click **Save**
11. Click **Submit**

---

## Employee Incentive

**URL:** `/app/employee-incentive`

**Workspace:** Payroll

Employee Incentive records performance-based bonuses.

### Employee Incentive Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Employee reference |
| Company | Yes | Link | Company |
| Incentive Amount | Yes | Currency | Bonus amount |
| Payroll Date | Yes | Date | When to pay |
| Salary Component | Yes | Link | Earning component |

### How to Create Employee Incentive
1. Click **Sidebar** → **Payroll**
2. Click **Employee Incentive** in shortcuts
3. Click **+ Add Employee Incentive**
4. Select **Employee**
5. Select **Company**
6. Enter **Incentive Amount**
7. Select **Payroll Date**
8. Select **Salary Component** (e.g., "Performance Bonus")
9. Click **Save**
10. Click **Submit**

---

## Payroll Settings

**URL:** `/app/payroll-settings`

**Workspace:** Payroll

### Payroll Settings Fields

| Field | Description |
|-------|-------------|
| Calculate Payroll Working Days Based On | Leave/Attendance |
| Max Working Hours Against Timesheet | For timesheet-based pay |
| Include Holidays In Total Working Days | Count holidays |
| Disable Rounded Total | Show exact amounts |
| Email Salary Slip To Employee | Auto-email payslips |
| Encrypt Salary Slips In Emails | Password-protect PDFs |
| Password Policy | Password generation rule |

### How to Configure Payroll Settings
1. Press `Ctrl + K` → type "Payroll Settings"
2. Click **Payroll Settings**
3. Configure options:
   - Select **Calculate Payroll Working Days Based On**
   - Check **Include Holidays In Total Working Days** if needed
   - Check **Email Salary Slip To Employee** for auto-email
   - Check **Encrypt Salary Slips In Emails** for security
4. Click **Save**

---

## Payroll Period

**URL:** `/app/payroll-period`

**Workspace:** Payroll

Payroll Period defines the fiscal year for payroll and tax calculations.

### Payroll Period Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Name | Yes | Data | Period name |
| Company | Yes | Link | Company |
| Start Date | Yes | Date | Period start |
| End Date | Yes | Date | Period end |

### How to Create Payroll Period
1. Click **Sidebar** → **Payroll**
2. Click **Payroll Period** in shortcuts
3. Click **+ Add Payroll Period**
4. Enter **Name** (e.g., "FY 2024")
5. Select **Company**
6. Select **Start Date** (e.g., 2024-01-01)
7. Select **End Date** (e.g., 2024-12-31)
8. Click **Save**

---

## Payroll Reports

**Workspace:** Payroll

### Available Reports

| Report | URL | Description |
|--------|-----|-------------|
| Salary Register | `/app/query-report/Salary Register` | All salary slips summary |
| Bank Remittance | `/app/query-report/Bank Remittance` | Bank payment file |
| Salary Payments Based On Payment Mode | `/app/query-report/Salary Payments Based On Payment Mode` | By payment method |
| Salary Payments via ECS | `/app/query-report/Salary Payments via ECS` | Electronic clearing |
| Income Tax Deductions | `/app/query-report/Income Tax Deductions` | Tax deduction summary |

### How to View Salary Register
1. Click **Sidebar** → **Payroll**
2. Click **Salary Register** in Reports
3. Select **From Date** and **To Date**
4. Select **Company**
5. Optionally filter by **Employee**, **Department**
6. View salary summary with all components

### How to Generate Bank Remittance
1. Click **Sidebar** → **Payroll**
2. Click **Bank Remittance** in Reports
3. Select **From Date** and **To Date**
4. Select **Company**
5. View bank transfer details
6. Click **Export** for bank file

---

## Quick Reference

### Payroll Processing Checklist
- [ ] Salary Components created
- [ ] Salary Structure created
- [ ] Salary Structure assigned to employees
- [ ] Additional Salary entries (if any)
- [ ] Create Payroll Entry
- [ ] Get Employees
- [ ] Create Salary Slips
- [ ] Review Salary Slips
- [ ] Submit Salary Slips
- [ ] Create Bank Entry

### Key URLs

| Document | URL |
|----------|-----|
| Salary Component | `/app/salary-component` |
| Salary Structure | `/app/salary-structure` |
| Salary Structure Assignment | `/app/salary-structure-assignment` |
| Payroll Entry | `/app/payroll-entry` |
| Salary Slip | `/app/salary-slip` |
| Additional Salary | `/app/additional-salary` |
| Employee Incentive | `/app/employee-incentive` |
| Payroll Settings | `/app/payroll-settings` |
| Payroll Period | `/app/payroll-period` |

### Required Roles
| Action | Required Role |
|--------|---------------|
| View own salary slip | Employee |
| Create salary components | HR Manager |
| Create salary structures | HR Manager |
| Process payroll | HR Manager |
| Submit salary slips | HR Manager |
| Create bank entry | HR Manager, Accounts Manager |
