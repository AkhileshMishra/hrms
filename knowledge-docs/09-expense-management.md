# Expense Management

## Overview
This guide covers expense claims, employee advances, travel requests, fleet management, and related reports.

---

## Expense Claim

**URL:** `/app/expense-claim`

**Workspace:** Expense Claims

Expense Claim allows employees to request reimbursement for business expenses.

### Expense Claim Fields

| Section | Field | Required | Description |
|---------|-------|----------|-------------|
| **Basic** | Employee | Yes | Employee reference |
| | Expense Approver | Yes | Approving manager |
| | Approval Status | Auto | Pending/Approved/Rejected |
| | Company | Yes | Company |
| | Posting Date | Yes | Claim date |
| **Expenses** | Expenses | Yes | Table of expense items |
| **Totals** | Total Claimed Amount | Auto | Sum of expenses |
| | Total Sanctioned Amount | Auto | Approved amount |
| | Total Amount Reimbursed | Auto | Paid amount |
| **Advance** | Employee Advance | No | Link to advance |
| | Total Advance Amount | Auto | Advance used |

### Expenses Table Fields

| Field | Required | Description |
|-------|----------|-------------|
| Expense Date | Yes | Date of expense |
| Expense Type | Yes | Category of expense |
| Description | No | Expense details |
| Amount | Yes | Claimed amount |
| Sanctioned Amount | Auto | Approved amount |
| Attach Receipt | No | Upload receipt |

### How to Submit Expense Claim (Employee View)
1. Click **Sidebar** → **Expense Claims**
2. Click **Expense Claim** in shortcuts
3. Click **+ Add Expense Claim**
4. **Employee** auto-fills with your name
5. **Expense Approver** auto-fills based on Reports To
6. Select **Company**
7. Select **Posting Date**
8. In **Expenses** table:
   - Click **Add Row**
   - Select **Expense Date**
   - Select **Expense Type** (e.g., "Travel", "Meals")
   - Enter **Description**
   - Enter **Amount**
   - Click **Attach Receipt** → upload receipt image
   - Repeat for each expense
9. Review **Total Claimed Amount**
10. Click **Save**
11. Click **Submit**

### How to Approve Expense Claim (Approver View)
1. Click **Sidebar** → **Expense Claims**
2. Click **Expense Claim** in shortcuts
3. Click **Filters** → **Approval Status** → "Pending"
4. Click **Filters** → **Expense Approver** → your name
5. Open the expense claim
6. Review each expense:
   - Check expense date and type
   - Verify description
   - Review attached receipts
   - Adjust **Sanctioned Amount** if needed
7. Click **Approve** button
8. Or click **Reject** with reason

### How to Reject Expense Claim
1. Open the expense claim
2. Review expenses
3. Click **Reject** button
4. Enter **Reason for Rejection**
5. Click **Reject**
6. Employee is notified of rejection

### How to Process Expense Payment
1. Open approved expense claim
2. Click **Make Payment Entry** (or **Create** → **Payment Entry**)
3. Select **Payment Account** (bank/cash)
4. Verify **Paid Amount**
5. Click **Save**
6. Click **Submit**
7. Expense claim shows as reimbursed

---

## Expense Claim Type

**URL:** `/app/expense-claim-type`

**Workspace:** Expense Claims

Expense Claim Type defines categories of expenses with optional default accounts.

### Expense Claim Type Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Expense Type | Yes | Data | Category name |
| Description | No | Text | Category description |
| Accounts | No | Table | GL account mapping |

### How to Create Expense Claim Type
1. Click **Sidebar** → **Expense Claims**
2. Click **Expense Claim Type** in shortcuts
3. Click **+ Add Expense Claim Type**
4. Enter **Expense Type** (e.g., "Travel - Airfare")
5. Enter **Description** (optional)
6. In **Accounts** table (optional):
   - Click **Add Row**
   - Select **Company**
   - Select **Default Account**
7. Click **Save**

### Common Expense Types

| Type | Description |
|------|-------------|
| Travel - Airfare | Flight tickets |
| Travel - Hotel | Accommodation |
| Travel - Ground Transport | Taxi, train, bus |
| Meals - Client | Client entertainment |
| Meals - Team | Team meals |
| Office Supplies | Stationery, etc. |
| Communication | Phone, internet |
| Training | Courses, certifications |
| Miscellaneous | Other expenses |

---

## Employee Advance

**URL:** `/app/employee-advance`

**Workspace:** Expense Claims

Employee Advance provides upfront payment to employees for anticipated expenses.

### Employee Advance Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Employee reference |
| Company | Yes | Link | Company |
| Purpose | Yes | Text | Reason for advance |
| Advance Amount | Yes | Currency | Requested amount |
| Posting Date | Yes | Date | Request date |
| Advance Account | Yes | Link | GL account |
| Mode of Payment | Yes | Link | Payment method |
| Status | Auto | Select | Draft/Submitted/Paid/Claimed/Returned |
| Paid Amount | Auto | Currency | Amount disbursed |
| Claimed Amount | Auto | Currency | Used in expense claims |
| Return Amount | Auto | Currency | Amount to return |

### How to Request Employee Advance (Employee)
1. Click **Sidebar** → **Expense Claims**
2. Click **Employee Advance** in shortcuts
3. Click **+ Add Employee Advance**
4. **Employee** auto-fills
5. Select **Company**
6. Enter **Purpose** (e.g., "Business trip to Jakarta")
7. Enter **Advance Amount**
8. Select **Posting Date**
9. Select **Advance Account**
10. Select **Mode of Payment**
11. Click **Save**
12. Click **Submit**

### How to Approve and Pay Advance (HR/Finance)
1. Click **Sidebar** → **Expense Claims**
2. Click **Employee Advance**
3. Filter by **Status** → "Submitted"
4. Open the advance request
5. Review purpose and amount
6. Click **Create Payment Entry**
7. Verify payment details
8. Click **Save** and **Submit** payment
9. Advance status changes to "Paid"

### How to Link Advance to Expense Claim
1. Create new expense claim
2. In **Employee Advance** field, select the advance
3. **Total Advance Amount** shows available balance
4. Add expenses
5. System calculates:
   - If expenses < advance: Return amount due
   - If expenses > advance: Additional reimbursement due
6. Submit expense claim

### How to Return Unused Advance
1. Open the employee advance
2. Click **Create Return Entry**
3. Enter **Return Amount**
4. Select payment method
5. Click **Save** and **Submit**
6. Advance status updates

---

## Travel Request

**URL:** `/app/travel-request`

**Workspace:** Expense Claims

Travel Request manages business travel approvals with itinerary and cost estimates.

### Travel Request Fields

| Section | Field | Required | Description |
|---------|-------|----------|-------------|
| **Basic** | Employee | Yes | Employee reference |
| | Travel Type | Yes | Domestic/International |
| | Purpose of Travel | Yes | Business reason |
| | Description | No | Additional details |
| **Itinerary** | Travel Itinerary | Yes | Table of travel legs |
| **Costing** | Costing Details | No | Table of estimated costs |
| | Total Costing | Auto | Sum of costs |

### Travel Itinerary Table

| Field | Required | Description |
|-------|----------|-------------|
| Departure Date | Yes | Travel start date |
| Departure Time | No | Departure time |
| Source Location | Yes | From city/location |
| Destination | Yes | To city/location |
| Mode of Travel | Yes | Flight/Train/Bus/Car |
| Arrival Date | Yes | Arrival date |
| Arrival Time | No | Arrival time |
| Lodging Required | No | Need accommodation |

### Costing Details Table

| Field | Required | Description |
|-------|----------|-------------|
| Expense Type | Yes | Cost category |
| Description | No | Cost details |
| Funded By | No | Company/Employee |
| Estimated Amount | Yes | Expected cost |

### How to Submit Travel Request (Employee)
1. Click **Sidebar** → **Expense Claims**
2. Click **Travel Request** in shortcuts
3. Click **+ Add Travel Request**
4. **Employee** auto-fills
5. Select **Travel Type** (Domestic/International)
6. Enter **Purpose of Travel**
7. Enter **Description** (optional)

   **Add Itinerary:**
8. In **Travel Itinerary** table, click **Add Row**
9. Select **Departure Date**
10. Enter **Source Location**
11. Enter **Destination**
12. Select **Mode of Travel**
13. Select **Arrival Date**
14. Check **Lodging Required** if needed
15. Add more legs if multi-city trip

    **Add Costing:**
16. In **Costing Details** table, click **Add Row**
17. Select **Expense Type** (Airfare/Hotel/etc.)
18. Enter **Description**
19. Select **Funded By**
20. Enter **Estimated Amount**
21. Add all expected costs
22. Review **Total Costing**
23. Click **Save**
24. Click **Submit**

### How to Approve Travel Request (Manager)
1. Click **Sidebar** → **Expense Claims**
2. Click **Travel Request**
3. Filter by **Status** → "Submitted"
4. Open the request
5. Review:
   - Purpose and dates
   - Itinerary details
   - Cost estimates
6. Click **Approve** or **Reject**

---

## Fleet Management

### Vehicle

**URL:** `/app/vehicle`

**Workspace:** Expense Claims

Vehicle tracks company vehicles for fleet management.

#### Vehicle Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| License Plate | Yes | Data | Vehicle registration |
| Make | Yes | Data | Manufacturer |
| Model | Yes | Data | Vehicle model |
| Fuel Type | No | Select | Petrol/Diesel/Electric |
| Acquisition Date | No | Date | Purchase date |
| Odometer Value | No | Int | Current mileage |
| Chassis No | No | Data | VIN number |
| Vehicle Value | No | Currency | Purchase price |
| Insurance Company | No | Data | Insurer |
| Policy No | No | Data | Insurance policy |
| Insurance Expiry | No | Date | Policy expiry |
| Employee | No | Link | Assigned employee |

#### How to Add a Vehicle
1. Click **Sidebar** → **Expense Claims**
2. Click **Vehicle** in shortcuts
3. Click **+ Add Vehicle**
4. Enter **License Plate**
5. Enter **Make** (e.g., "Toyota")
6. Enter **Model** (e.g., "Camry")
7. Select **Fuel Type**
8. Enter **Acquisition Date**
9. Enter **Odometer Value**
10. Enter insurance details:
    - **Insurance Company**
    - **Policy No**
    - **Insurance Expiry**
11. Select **Employee** (if assigned)
12. Click **Save**

### Vehicle Log

**URL:** `/app/vehicle-log`

**Workspace:** Expense Claims

Vehicle Log records vehicle usage, mileage, and expenses.

#### Vehicle Log Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| License Plate | Yes | Link | Vehicle reference |
| Employee | Yes | Link | Driver |
| Date | Yes | Date | Log date |
| Odometer Reading | Yes | Int | Current mileage |
| Model | Auto | Data | From vehicle |
| Make | Auto | Data | From vehicle |
| Fuel Qty | No | Float | Fuel added |
| Price | No | Currency | Fuel cost |
| Service Detail | No | Text | Service notes |
| Service Expense | No | Table | Service costs |

#### How to Create Vehicle Log
1. Click **Sidebar** → **Expense Claims**
2. Click **Vehicle Log** in shortcuts
3. Click **+ Add Vehicle Log**
4. Select **License Plate**
5. Select **Employee** (driver)
6. Select **Date**
7. Enter **Odometer Reading**
8. Enter fuel details (if refueling):
   - **Fuel Qty**
   - **Price**
9. Enter **Service Detail** (if serviced)
10. In **Service Expense** table (if applicable):
    - Click **Add Row**
    - Select **Expense Type**
    - Enter **Amount**
11. Click **Save**

### How to View Fleet Reports
1. Click **Sidebar** → **Expense Claims**
2. Click **Vehicle Expenses** in Reports
3. Select **Vehicle** (or all)
4. Select date range
5. View:
   - Fuel expenses
   - Service costs
   - Total by vehicle

---

## Expense Reports

**Workspace:** Expense Claims

### Available Reports

| Report | URL | Description |
|--------|-----|-------------|
| Expense Claim Summary | `/app/query-report/Expense Claim Summary` | Claims by employee/type |
| Employee Advance Summary | `/app/query-report/Employee Advance Summary` | Advance status |
| Vehicle Expenses | `/app/query-report/Vehicle Expenses` | Fleet costs |

### How to View Expense Claim Summary
1. Click **Sidebar** → **Expense Claims**
2. Click **Expense Claim Summary** in Reports
3. Select **Company**
4. Select **From Date** and **To Date**
5. Optionally filter by **Employee**, **Expense Type**
6. View summary:
   - Total claimed
   - Total approved
   - Total reimbursed

### How to Export Expense Report
1. Open any expense report
2. Click **Menu** (⋮) → **Export**
3. Select format (Excel/CSV)
4. Click **Export**

---

## Quick Reference

### Expense Claim Status Flow
```
Draft → Submitted → Approved/Rejected → Paid (if approved)
```

### Employee Advance Status Flow
```
Draft → Submitted → Paid → Claimed/Returned
```

### Key URLs

| Document | URL |
|----------|-----|
| Expense Claim | `/app/expense-claim` |
| Expense Claim Type | `/app/expense-claim-type` |
| Employee Advance | `/app/employee-advance` |
| Travel Request | `/app/travel-request` |
| Vehicle | `/app/vehicle` |
| Vehicle Log | `/app/vehicle-log` |

### Expense Management Checklist
- [ ] Create Expense Claim Types
- [ ] Set up expense approvers (Reports To)
- [ ] Configure expense accounts
- [ ] Add vehicles (if fleet management needed)
- [ ] Train employees on expense submission

### Required Roles
| Action | Required Role |
|--------|---------------|
| Submit expense claim | Employee |
| Approve expense claim | Expense Approver, HR Manager |
| Process payment | HR Manager, Accounts |
| Request advance | Employee |
| Approve advance | HR Manager |
| Manage vehicles | Fleet Manager |
| Create vehicle logs | Employee, Fleet Manager |
