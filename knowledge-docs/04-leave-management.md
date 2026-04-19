# Leave Management

## Overview
This guide covers complete leave management including leave types, policies, allocations, applications, approvals, and all leave-related features.

---

## Leave Type Setup

**URL:** `/app/leave-type`

**Workspace:** Leaves

Leave Types define the categories of leave available to employees.

### Leave Type Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Leave Type Name | Yes | Data | Name of leave type |
| Max Leaves Allowed | No | Int | Maximum days per period |
| Applicable After (Days) | No | Int | Days after joining before eligible |
| Max Continuous Days | No | Int | Maximum consecutive days |
| Is Carry Forward | No | Check | Allow unused leaves to carry forward |
| Is Leave Without Pay | No | Check | Unpaid leave type |
| Is Optional Leave | No | Check | Optional/floating holiday |
| Allow Negative Balance | No | Check | Allow overdraft |
| Include Holiday Within Leaves | No | Check | Count holidays in leave duration |
| Is Compensatory | No | Check | For compensatory off |

### Carry Forward Settings

| Field | Description |
|-------|-------------|
| Is Carry Forward | Enable carry forward |
| Maximum Carry Forwarded Leaves | Limit on carried leaves |
| Expire Carry Forwarded Leaves After (Days) | Auto-expire after days |

### Encashment Settings

| Field | Description |
|-------|-------------|
| Allow Encashment | Enable leave encashment |
| Encashment Threshold Days | Minimum balance to encash |
| Earning Component | Salary component for encashment |

### Earned Leave Settings

| Field | Description |
|-------|-------------|
| Is Earned Leave | Enable earned leave |
| Earned Leave Frequency | Monthly/Quarterly/Yearly |
| Rounding | 0.5/1.0 rounding |

### How to Create a Leave Type
1. Click **Sidebar** → **Leaves**
2. Click **Leave Type** in shortcuts
3. Click **+ Add Leave Type**
4. Enter **Leave Type Name** (e.g., "Annual Leave")
5. Enter **Max Leaves Allowed** (e.g., 14)
6. Configure options:

   **For Carry Forward:**
   - Check **Is Carry Forward**
   - Enter **Maximum Carry Forwarded Leaves**
   - Enter **Expire Carry Forwarded Leaves After (Days)**

   **For Encashment:**
   - Check **Allow Encashment**
   - Enter **Encashment Threshold Days**
   - Select **Earning Component**

   **For Earned Leave:**
   - Check **Is Earned Leave**
   - Select **Earned Leave Frequency**
   - Select **Rounding**

7. Click **Save**

### Common Leave Types to Create

| Leave Type | Max Days | Carry Forward | Encashment | Earned |
|------------|----------|---------------|------------|--------|
| Annual Leave | 14 | Yes | Yes | No |
| Sick Leave | 14 | No | No | No |
| Medical Leave | 60 | No | No | No |
| Maternity Leave | 112 | No | No | No |
| Paternity Leave | 14 | No | No | No |
| Compassionate Leave | 3 | No | No | No |
| Marriage Leave | 3 | No | No | No |
| Unpaid Leave | 365 | No | No | No |
| Compensatory Off | 30 | No | No | No |

---

## Leave Policy

**URL:** `/app/leave-policy`

**Workspace:** Leaves

Leave Policy defines leave allocations for a group of employees.

### Leave Policy Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Leave Policy Name | Yes | Data | Policy identifier |
| Leave Policy Details | Yes | Table | Leave types and allocations |

### Leave Policy Details Table

| Field | Required | Description |
|-------|----------|-------------|
| Leave Type | Yes | Type of leave |
| Annual Allocation | Yes | Days allocated per year |

### How to Create a Leave Policy
1. Click **Sidebar** → **Leaves**
2. Click **Leave Policy** in shortcuts
3. Click **+ Add Leave Policy**
4. Enter **Leave Policy Name** (e.g., "Standard Employee Policy")
5. In **Leave Policy Details** table:
   - Click **Add Row**
   - Select **Leave Type** (e.g., "Annual Leave")
   - Enter **Annual Allocation** (e.g., 14)
   - Repeat for each leave type
6. Click **Save**

---

## Leave Period

**URL:** `/app/leave-period`

**Workspace:** Leaves

Leave Period defines the time frame for leave allocations (typically a year).

### Leave Period Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| From Date | Yes | Date | Period start |
| To Date | Yes | Date | Period end |
| Company | Yes | Link | Applicable company |
| Is Active | No | Check | Current active period |

### How to Create a Leave Period
1. Click **Sidebar** → **Leaves**
2. Click **Leave Period** in shortcuts
3. Click **+ Add Leave Period**
4. Select **From Date** (e.g., 2024-01-01)
5. Select **To Date** (e.g., 2024-12-31)
6. Select **Company**
7. Check **Is Active** for current period
8. Click **Save**

---

## Leave Allocation

**URL:** `/app/leave-allocation`

**Workspace:** Leaves

Leave Allocation assigns leave balance to individual employees.

### Leave Allocation Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Employee reference |
| Leave Type | Yes | Link | Type of leave |
| From Date | Yes | Date | Allocation start |
| To Date | Yes | Date | Allocation end |
| New Leaves Allocated | Yes | Float | Number of days |
| Carry Forward | No | Check | Include carried leaves |
| Carry Forwarded Leaves | Auto | Float | Days carried forward |

### How to Create Leave Allocation (Individual)
1. Click **Sidebar** → **Leaves**
2. Click **Leave Allocation** in shortcuts
3. Click **+ Add Leave Allocation**
4. Select **Employee**
5. Select **Leave Type**
6. Select **From Date**
7. Select **To Date**
8. Enter **New Leaves Allocated**
9. Check **Carry Forward** if applicable
10. Click **Save**
11. Click **Submit** to activate

---

## Leave Policy Assignment

**URL:** `/app/leave-policy-assignment`

**Workspace:** Leaves

Leave Policy Assignment links a leave policy to employees and auto-creates allocations.

### Leave Policy Assignment Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Employee reference |
| Leave Policy | Yes | Link | Policy to assign |
| Leave Period | Yes | Link | Applicable period |
| Effective From | Yes | Date | Assignment start date |
| Assignment Based On | No | Select | Leave Period/Joining Date |

### How to Assign Leave Policy (Individual)
1. Click **Sidebar** → **Leaves**
2. Click **Leave Policy Assignment** in shortcuts
3. Click **+ Add Leave Policy Assignment**
4. Select **Employee**
5. Select **Leave Policy**
6. Select **Leave Period**
7. Select **Effective From** date
8. Click **Save**
9. Click **Submit**
10. System auto-creates leave allocations

### How to Bulk Assign Leave Policy
1. Click **Sidebar** → **Leaves**
2. Click **Leave Policy Assignment** in shortcuts
3. Click **Menu** (⋮) → **Grant Leaves**
4. Select **Leave Policy**
5. Select **Leave Period**
6. Select **Company**
7. Optionally filter by **Department**, **Designation**, **Employee Grade**
8. Click **Grant**
9. System creates assignments for all matching employees

---

## Applying for Leave (Employee View)

**URL:** `/app/leave-application`

**Workspace:** Leaves

### Leave Application Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Auto-filled for self |
| Leave Type | Yes | Link | Type of leave |
| From Date | Yes | Date | Leave start date |
| To Date | Yes | Date | Leave end date |
| Half Day | No | Check | Half day leave |
| Half Day Date | Cond | Date | Which day is half |
| Reason | No | Text | Leave reason |
| Leave Approver | Yes | Link | Approving manager |

### How to Apply for Leave (Employee)
1. Click **Sidebar** → **Leaves**
2. Click **Leave Application** in shortcuts
3. Click **+ Add Leave Application**
4. **Employee** auto-fills with your name
5. Select **Leave Type** from dropdown
6. Click **From Date** → select start date
7. Click **To Date** → select end date
8. Check **Half Day** if applicable
   - If checked, select **Half Day Date**
9. Enter **Reason** for leave
10. **Leave Approver** auto-fills based on Reports To
11. Review **Total Leave Days** (auto-calculated)
12. Click **Save**
13. Click **Submit** to send for approval

### How to Check Leave Balance
1. Click **Sidebar** → **Leaves**
2. Click **Leave Balance** report in shortcuts
3. Or go to `/app/query-report/Employee Leave Balance`
4. Select your **Employee** (or auto-filtered)
5. View balance by leave type

---

## Approving Leave (Manager View)

### How to View Pending Leave Requests
1. Click **Sidebar** → **Leaves**
2. Click **Leave Application** in shortcuts
3. Click **Filters** → **Status** → "Open"
4. Click **Filters** → **Leave Approver** → your name
5. View all pending requests

### How to Approve Leave
1. Open the leave application
2. Review details:
   - Employee name
   - Leave type
   - Dates and duration
   - Reason
   - Leave balance
3. Click **Approve** button
4. Or click **Actions** → **Approve**
5. Leave status changes to "Approved"

### How to Reject Leave
1. Open the leave application
2. Review details
3. Click **Reject** button
4. Enter **Reason for Rejection** (optional)
5. Click **Reject**
6. Leave status changes to "Rejected"

---

## Compensatory Leave

**URL:** `/app/compensatory-leave-request`

**Workspace:** Leaves

Compensatory leave is granted for working on holidays or rest days.

### Compensatory Leave Request Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Employee reference |
| Work From Date | Yes | Date | Start of extra work |
| Work End Date | Yes | Date | End of extra work |
| Reason | No | Text | Reason for comp off |
| Leave Type | Yes | Link | Compensatory leave type |

### How to Request Compensatory Leave
1. Click **Sidebar** → **Leaves**
2. Click **Compensatory Leave Request** in shortcuts
3. Click **+ Add Compensatory Leave Request**
4. Select **Employee** (or auto-filled)
5. Select **Work From Date** (the holiday/rest day worked)
6. Select **Work End Date**
7. Enter **Reason**
8. Select **Leave Type** (must be marked as Compensatory)
9. Click **Save**
10. Click **Submit**
11. After approval, leave balance is credited

---

## Leave Encashment

**URL:** `/app/leave-encashment`

**Workspace:** Leaves

Leave Encashment converts unused leave balance to cash.

### Leave Encashment Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Employee reference |
| Leave Type | Yes | Link | Leave type to encash |
| Leave Period | Yes | Link | Applicable period |
| Encashment Date | Yes | Date | Date of encashment |
| Encashable Days | Auto | Float | Days available to encash |
| Encashment Amount | Auto | Currency | Calculated amount |

### How to Process Leave Encashment
1. Click **Sidebar** → **Leaves**
2. Click **Leave Encashment** in shortcuts
3. Click **+ Add Leave Encashment**
4. Select **Employee**
5. Select **Leave Type** (must allow encashment)
6. Select **Leave Period**
7. Select **Encashment Date**
8. **Encashable Days** auto-calculates
9. **Encashment Amount** auto-calculates based on salary
10. Click **Save**
11. Click **Submit**
12. Creates Additional Salary entry

---

## Leave Block List

**URL:** `/app/leave-block-list`

**Workspace:** Leaves

Leave Block List prevents leave applications on specific dates.

### Leave Block List Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Leave Block List Name | Yes | Data | List identifier |
| Company | Yes | Link | Applicable company |
| Block Days | Yes | Table | Dates to block |
| Applies To All Departments | No | Check | Company-wide block |
| Allowed | No | Table | Users who can override |

### How to Create Leave Block List
1. Click **Sidebar** → **Leaves**
2. Click **Leave Block List** in shortcuts
3. Click **+ Add Leave Block List**
4. Enter **Leave Block List Name** (e.g., "Year End Block")
5. Select **Company**
6. In **Block Days** table:
   - Click **Add Row**
   - Select **Block Date**
   - Enter **Reason**
7. Check **Applies To All Departments** or select specific departments
8. In **Allowed** table, add users who can still apply
9. Click **Save**

---

## Leave Control Panel

**URL:** `/app/leave-control-panel`

**Workspace:** Leaves

Leave Control Panel provides bulk leave allocation operations.

### How to Use Leave Control Panel
1. Click **Sidebar** → **Leaves**
2. Click **Leave Control Panel** in shortcuts
3. Select filters:
   - **Company**
   - **Employment Type**
   - **Branch**
   - **Department**
   - **Designation**
   - **Employee Grade**
4. Select **Leave Type**
5. Select **From Date** and **To Date**
6. Enter **No of Days** to allocate
7. Check **Add To Existing** to add to current balance
8. Click **Allocate**

---

## Leave Reports

**Workspace:** Leaves

### Available Leave Reports

| Report | URL | Description |
|--------|-----|-------------|
| Employee Leave Balance | `/app/query-report/Employee Leave Balance` | Current leave balances |
| Employee Leave Balance Summary | `/app/query-report/Employee Leave Balance Summary` | Summary by leave type |
| Leave Application Trends | `/app/query-report/Leave Application Trends` | Leave patterns over time |
| Leave Ledger | `/app/leave-ledger-entry` | Detailed leave transactions |

### How to Access Leave Reports
1. Click **Sidebar** → **Leaves**
2. Scroll to **Reports** section
3. Click desired report name
4. Set filters (Employee, Date Range, Leave Type)
5. Click **Refresh** or report auto-loads

### How to View Employee Leave Balance Report
1. Click **Sidebar** → **Leaves**
2. Click **Employee Leave Balance** in Reports
3. Select **Company**
4. Select **Employee** (optional, for specific employee)
5. Select **From Date** and **To Date**
6. View balance by leave type

### How to Export Leave Report
1. Open any leave report
2. Click **Menu** (⋮) → **Export**
3. Select format (Excel/CSV)
4. Click **Export**

---

## Quick Reference

### Leave Application Status Flow
```
Draft → Open (Submitted) → Approved/Rejected → Cancelled (if needed)
```

### Key URLs

| Document | URL |
|----------|-----|
| Leave Type | `/app/leave-type` |
| Leave Policy | `/app/leave-policy` |
| Leave Period | `/app/leave-period` |
| Leave Allocation | `/app/leave-allocation` |
| Leave Policy Assignment | `/app/leave-policy-assignment` |
| Leave Application | `/app/leave-application` |
| Compensatory Leave Request | `/app/compensatory-leave-request` |
| Leave Encashment | `/app/leave-encashment` |
| Leave Block List | `/app/leave-block-list` |

### Leave Setup Checklist
- [ ] Create Leave Types
- [ ] Create Leave Period
- [ ] Create Leave Policy
- [ ] Assign Leave Policy to Employees
- [ ] Verify Leave Allocations created

### Required Roles
| Action | Required Role |
|--------|---------------|
| Apply for leave | Employee |
| Approve leave | Leave Approver, HR Manager |
| Create leave types | HR Manager |
| Allocate leaves | HR User, HR Manager |
| Process encashment | HR Manager |
