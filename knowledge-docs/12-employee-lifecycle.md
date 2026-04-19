# Employee Lifecycle Management

## Overview
This guide covers the complete employee journey from onboarding to exit, including promotions, transfers, separations, grievances, and training.

---

## Employee Onboarding

**URL:** `/app/employee-onboarding`

**Workspace:** Employee Lifecycle

Employee Onboarding manages the new hire orientation process with task checklists.

### Onboarding Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | New employee |
| Employee Name | Auto | Data | From employee |
| Company | Yes | Link | Company |
| Department | Auto | Link | From employee |
| Designation | Auto | Link | From employee |
| Date of Joining | Auto | Date | From employee |
| Employee Onboarding Template | Yes | Link | Task template |
| Status | Yes | Select | Pending/In Progress/Completed |
| Activities | Yes | Table | Onboarding tasks |

### Activities Table

| Field | Required | Description |
|-------|----------|-------------|
| Activity Name | Yes | Task name |
| User | No | Responsible person |
| Role | No | Responsible role |
| Required For Employee Creation | No | Block employee creation |
| Begin On | No | Days after joining |
| Duration | No | Days to complete |
| Status | Yes | Pending/Completed |

### How to Create Onboarding Template
1. Press `Ctrl + K` → type "Employee Onboarding Template"
2. Click **+ Add Employee Onboarding Template**
3. Enter **Template Name** (e.g., "Standard Onboarding")
4. Select **Company**
5. In **Activities** table:
   - Click **Add Row**
   - Enter **Activity Name** (e.g., "IT Setup")
   - Select **User** or **Role** responsible
   - Enter **Begin On** (days after joining)
   - Enter **Duration** (days)
   - Repeat for all tasks
6. Click **Save**

### Sample Onboarding Tasks

| Task | Responsible | Begin | Duration |
|------|-------------|-------|----------|
| Welcome email | HR | 0 | 1 |
| IT equipment setup | IT | 0 | 1 |
| System access creation | IT | 0 | 1 |
| HR documentation | HR | 0 | 3 |
| Team introduction | Manager | 1 | 1 |
| Policy orientation | HR | 1 | 2 |
| Role-specific training | Manager | 3 | 5 |
| 30-day check-in | HR | 30 | 1 |

### How to Create Employee Onboarding
1. Click **Sidebar** → **Employee Lifecycle**
2. Click **Employee Onboarding** in shortcuts
3. Click **+ Add Employee Onboarding**
4. Select **Employee**
5. Select **Company**
6. Select **Employee Onboarding Template**
7. **Activities** auto-populate from template
8. Adjust tasks if needed
9. Click **Save**
10. Click **Submit**

### How to Complete Onboarding Tasks
1. Open the employee onboarding record
2. In **Activities** table:
   - Find your assigned task
   - Change **Status** to "Completed"
3. Click **Save**
4. When all tasks complete, change overall **Status** to "Completed"

---

## Employee Promotion

**URL:** `/app/employee-promotion`

**Workspace:** Employee Lifecycle

Employee Promotion records advancement in designation, grade, or department.

### Promotion Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Employee reference |
| Company | Yes | Link | Company |
| Promotion Date | Yes | Date | Effective date |
| Promotion Details | Yes | Table | Changes to apply |

### Promotion Details Table

| Field | Required | Description |
|-------|----------|-------------|
| Property | Yes | Field to change |
| Current | Auto | Current value |
| New | Yes | New value |

### How to Process Employee Promotion
1. Click **Sidebar** → **Employee Lifecycle**
2. Click **Employee Promotion** in shortcuts
3. Click **+ Add Employee Promotion**
4. Select **Employee**
5. Select **Company**
6. Select **Promotion Date**
7. In **Promotion Details** table:
   - Click **Add Row**
   - Select **Property** → "Designation"
   - **Current** shows current designation
   - Select **New** designation
   - Add row for "Employee Grade" if changing
   - Add row for "Department" if transferring
8. Click **Save**
9. Click **Submit**
10. Employee record updates automatically on promotion date

---

## Employee Transfer

**URL:** `/app/employee-transfer`

**Workspace:** Employee Lifecycle

Employee Transfer records movement between departments, branches, or companies.

### Transfer Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Employee reference |
| Company | Yes | Link | Current company |
| New Company | No | Link | If inter-company |
| Transfer Date | Yes | Date | Effective date |
| Transfer Details | Yes | Table | Changes to apply |

### Transfer Details Table

| Field | Required | Description |
|-------|----------|-------------|
| Property | Yes | Field to change |
| Current | Auto | Current value |
| New | Yes | New value |

### How to Process Employee Transfer
1. Click **Sidebar** → **Employee Lifecycle**
2. Click **Employee Transfer** in shortcuts
3. Click **+ Add Employee Transfer**
4. Select **Employee**
5. Select **Company**
6. Select **New Company** (if inter-company transfer)
7. Select **Transfer Date**
8. In **Transfer Details** table:
   - Click **Add Row**
   - Select **Property** → "Department"
   - **Current** shows current department
   - Select **New** department
   - Add row for "Branch" if changing location
   - Add row for "Reports To" if changing manager
9. Click **Save**
10. Click **Submit**
11. Employee record updates on transfer date

---

## Employee Separation

**URL:** `/app/employee-separation`

**Workspace:** Employee Lifecycle

Employee Separation manages the offboarding process when an employee leaves.

### Separation Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Departing employee |
| Company | Yes | Link | Company |
| Separation Date | Yes | Date | Last working day |
| Reason for Leaving | No | Text | Exit reason |
| Employee Separation Template | Yes | Link | Task template |
| Status | Yes | Select | Pending/In Progress/Completed |
| Activities | Yes | Table | Offboarding tasks |

### How to Create Separation Template
1. Press `Ctrl + K` → type "Employee Separation Template"
2. Click **+ Add Employee Separation Template**
3. Enter **Template Name** (e.g., "Standard Offboarding")
4. Select **Company**
5. In **Activities** table:
   - Click **Add Row**
   - Enter **Activity Name**
   - Select **User** or **Role**
   - Enter **Begin On** (days before/after separation)
   - Repeat for all tasks
6. Click **Save**

### Sample Separation Tasks

| Task | Responsible | Timing |
|------|-------------|--------|
| Resignation acceptance | HR | Day 0 |
| Knowledge transfer | Manager | Week 1-2 |
| Exit interview | HR | Last week |
| IT asset return | IT | Last day |
| Access revocation | IT | Last day |
| Final settlement | Finance | Last day |
| Experience letter | HR | Last day |
| Full & Final clearance | HR | After exit |

### How to Create Employee Separation
1. Click **Sidebar** → **Employee Lifecycle**
2. Click **Employee Separation** in shortcuts
3. Click **+ Add Employee Separation**
4. Select **Employee**
5. Select **Company**
6. Select **Separation Date** (last working day)
7. Enter **Reason for Leaving**
8. Select **Employee Separation Template**
9. **Activities** auto-populate
10. Click **Save**
11. Click **Submit**

### How to Complete Separation Tasks
1. Open the employee separation record
2. In **Activities** table:
   - Find your assigned task
   - Change **Status** to "Completed"
3. Click **Save**
4. When all tasks complete:
   - Change overall **Status** to "Completed"
   - Employee status changes to "Left"

---

## Exit Interview

**URL:** `/app/exit-interview`

**Workspace:** Employee Lifecycle

Exit Interview captures feedback from departing employees.

### Exit Interview Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Departing employee |
| Company | Yes | Link | Company |
| Date | Yes | Date | Interview date |
| Interviewer | Yes | Link | HR conducting interview |
| Status | Yes | Select | Pending/Scheduled/Completed |
| Interview Summary | No | Text | Key points |
| Questionnaire | No | Table | Q&A responses |

### How to Schedule Exit Interview
1. Click **Sidebar** → **Employee Lifecycle**
2. Click **Exit Interview** in shortcuts
3. Click **+ Add Exit Interview**
4. Select **Employee**
5. Select **Company**
6. Select **Date**
7. Select **Interviewer** (HR user)
8. Select **Status** → "Scheduled"
9. Click **Save**

### How to Complete Exit Interview
1. Open the exit interview
2. Conduct interview with employee
3. In **Questionnaire** table:
   - Click **Add Row**
   - Enter **Question**
   - Enter **Answer**
   - Repeat for all questions
4. Enter **Interview Summary**
5. Change **Status** to "Completed"
6. Click **Save**

### Common Exit Interview Questions

| Question |
|----------|
| What prompted your decision to leave? |
| What did you enjoy most about working here? |
| What could we improve? |
| How was your relationship with your manager? |
| Would you recommend this company to others? |
| Would you consider returning in the future? |

---

## Full and Final Statement

**URL:** `/app/full-and-final-statement`

**Workspace:** Employee Lifecycle

Full and Final Statement calculates the final settlement for departing employees.

### Full and Final Statement Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Departing employee |
| Company | Yes | Link | Company |
| Transaction Date | Yes | Date | Settlement date |
| Payables | Yes | Table | Amounts owed to employee |
| Receivables | Yes | Table | Amounts owed by employee |
| Total Payable | Auto | Currency | Sum of payables |
| Total Receivable | Auto | Currency | Sum of receivables |
| Net Amount | Auto | Currency | Final settlement |

### Payables Table

| Field | Required | Description |
|-------|----------|-------------|
| Component | Yes | Payment type |
| Amount | Yes | Amount owed |

### Receivables Table

| Field | Required | Description |
|-------|----------|-------------|
| Component | Yes | Recovery type |
| Amount | Yes | Amount to recover |

### How to Create Full and Final Statement
1. Click **Sidebar** → **Employee Lifecycle**
2. Click **Full and Final Statement** in shortcuts
3. Click **+ Add Full and Final Statement**
4. Select **Employee**
5. Select **Company**
6. Select **Transaction Date**
7. In **Payables** table:
   - Click **Add Row**
   - Select **Component** (e.g., "Pending Salary")
   - Enter **Amount**
   - Add: Leave encashment, Bonus, Gratuity, etc.
8. In **Receivables** table:
   - Click **Add Row**
   - Select **Component** (e.g., "Notice Period Recovery")
   - Enter **Amount**
   - Add: Loan recovery, Asset damage, etc.
9. Review **Net Amount**
10. Click **Save**
11. Click **Submit**

### Common Payable Components

| Component | Description |
|-----------|-------------|
| Pending Salary | Unpaid salary |
| Leave Encashment | Unused leave balance |
| Bonus | Pending bonus |
| Gratuity | Service gratuity |
| Reimbursements | Pending expense claims |

### Common Receivable Components

| Component | Description |
|-----------|-------------|
| Notice Period Recovery | Short notice deduction |
| Loan Recovery | Outstanding loans |
| Advance Recovery | Uncleared advances |
| Asset Recovery | Unreturned equipment |

---

## Employee Grievance

**URL:** `/app/employee-grievance`

**Workspace:** Employee Lifecycle

Employee Grievance tracks and resolves employee complaints.

### Grievance Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Subject | Yes | Data | Grievance title |
| Raised By | Yes | Link | Employee filing |
| Grievance Against | No | Link | Person/department |
| Company | Yes | Link | Company |
| Date | Yes | Date | Filing date |
| Status | Yes | Select | Open/Investigated/Resolved/Invalid |
| Grievance Type | No | Link | Category |
| Description | Yes | Text | Detailed complaint |
| Resolution | No | Text | Resolution details |
| Resolved By | No | Link | Resolver |
| Resolution Date | No | Date | When resolved |

### How to File Employee Grievance
1. Click **Sidebar** → **Employee Lifecycle**
2. Click **Employee Grievance** in shortcuts
3. Click **+ Add Employee Grievance**
4. Enter **Subject**
5. **Raised By** auto-fills (or select employee)
6. Select **Grievance Against** (optional)
7. Select **Company**
8. Select **Date**
9. Select **Grievance Type** (if configured)
10. Enter **Description** (detailed complaint)
11. Click **Save**
12. Click **Submit**

### How to Resolve Grievance (HR)
1. Click **Sidebar** → **Employee Lifecycle**
2. Click **Employee Grievance**
3. Filter by **Status** → "Open"
4. Open the grievance
5. Investigate the complaint
6. Change **Status** to "Investigated"
7. Enter **Resolution** details
8. Select **Resolved By**
9. Select **Resolution Date**
10. Change **Status** to "Resolved"
11. Click **Save**

---

## Training Program

**URL:** `/app/training-program`

**Workspace:** Employee Lifecycle

Training Program defines courses and learning paths for employees.

### Training Program Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Program Name | Yes | Data | Training title |
| Trainer Name | No | Data | Instructor |
| Trainer Email | No | Data | Instructor email |
| Supplier | No | Link | External provider |
| Description | No | Text | Program details |

### How to Create Training Program
1. Click **Sidebar** → **Employee Lifecycle**
2. Click **Training Program** in shortcuts
3. Click **+ Add Training Program**
4. Enter **Program Name** (e.g., "Leadership Development")
5. Enter **Trainer Name**
6. Enter **Trainer Email**
7. Select **Supplier** (if external)
8. Enter **Description**
9. Click **Save**

---

## Training Event

**URL:** `/app/training-event`

**Workspace:** Employee Lifecycle

Training Event schedules specific training sessions.

### Training Event Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Event Name | Yes | Data | Session title |
| Training Program | No | Link | Parent program |
| Type | Yes | Select | Seminar/Theory/Workshop |
| Level | No | Select | Beginner/Intermediate/Expert |
| Trainer Name | No | Data | Instructor |
| Start Time | Yes | Datetime | Session start |
| End Time | Yes | Datetime | Session end |
| Location | No | Data | Venue |
| Employees | Yes | Table | Attendees |

### How to Create Training Event
1. Click **Sidebar** → **Employee Lifecycle**
2. Click **Training Event** in shortcuts
3. Click **+ Add Training Event**
4. Enter **Event Name**
5. Select **Training Program** (optional)
6. Select **Type** (Seminar/Theory/Workshop)
7. Select **Level**
8. Enter **Trainer Name**
9. Select **Start Time**
10. Select **End Time**
11. Enter **Location**
12. In **Employees** table:
    - Click **Add Row**
    - Select **Employee**
    - Repeat for all attendees
13. Click **Save**
14. Click **Submit** (sends invites)

---

## Training Feedback

**URL:** `/app/training-feedback`

**Workspace:** Employee Lifecycle

Training Feedback captures attendee feedback on training sessions.

### How to Submit Training Feedback
1. Click **Sidebar** → **Employee Lifecycle**
2. Click **Training Feedback** in shortcuts
3. Click **+ Add Training Feedback**
4. Select **Training Event**
5. **Employee** auto-fills
6. Enter **Feedback** comments
7. Enter **Rating** (1-5)
8. Click **Save**
9. Click **Submit**

---

## Training Result

**URL:** `/app/training-result`

**Workspace:** Employee Lifecycle

Training Result records employee performance in training.

### How to Record Training Result
1. Click **Sidebar** → **Employee Lifecycle**
2. Click **Training Result** in shortcuts
3. Click **+ Add Training Result**
4. Select **Training Event**
5. Select **Employee**
6. Enter **Hours** attended
7. Enter **Grade** or **Score**
8. Enter **Comments**
9. Click **Save**

---

## Daily Work Summary

**URL:** `/app/daily-work-summary`

**Workspace:** Employee Lifecycle

Daily Work Summary tracks daily activities and accomplishments.

### How to Submit Daily Work Summary
1. Click **Sidebar** → **Employee Lifecycle**
2. Click **Daily Work Summary** in shortcuts
3. Click **+ Add Daily Work Summary**
4. **Employee** auto-fills
5. Select **Date**
6. Enter **Summary** of work done
7. Click **Save**
8. Click **Submit**

---

## Quick Reference

### Employee Lifecycle Flow
```
Recruitment → Onboarding → Active Employment → Promotion/Transfer → Separation → Exit
```

### Key URLs

| Document | URL |
|----------|-----|
| Employee Onboarding | `/app/employee-onboarding` |
| Employee Onboarding Template | `/app/employee-onboarding-template` |
| Employee Promotion | `/app/employee-promotion` |
| Employee Transfer | `/app/employee-transfer` |
| Employee Separation | `/app/employee-separation` |
| Employee Separation Template | `/app/employee-separation-template` |
| Exit Interview | `/app/exit-interview` |
| Full and Final Statement | `/app/full-and-final-statement` |
| Employee Grievance | `/app/employee-grievance` |
| Training Program | `/app/training-program` |
| Training Event | `/app/training-event` |
| Training Feedback | `/app/training-feedback` |
| Training Result | `/app/training-result` |
| Daily Work Summary | `/app/daily-work-summary` |

### Lifecycle Setup Checklist
- [ ] Create Onboarding Template
- [ ] Create Separation Template
- [ ] Configure grievance types
- [ ] Set up training programs
- [ ] Define exit interview questions

### Required Roles
| Action | Required Role |
|--------|---------------|
| Complete onboarding tasks | Assigned User |
| Process promotion | HR Manager |
| Process transfer | HR Manager |
| Process separation | HR Manager |
| Conduct exit interview | HR User, HR Manager |
| Create F&F statement | HR Manager |
| File grievance | Employee |
| Resolve grievance | HR Manager |
| Create training | HR User, HR Manager |
| Submit feedback | Employee |
