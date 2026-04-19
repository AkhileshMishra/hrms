# Employee Management

## Overview
This guide covers creating and managing employee records, including all field sections, Singapore-specific fields, employee lifecycle, skill mapping, and grading.

---

## Creating an Employee

**URL:** `/app/employee`

**Workspace:** HR

### How to Create a New Employee
1. Click **Sidebar** → **HR**
2. Click **Employee** in shortcuts
3. Click **+ Add Employee** button
4. Fill in all required fields (see sections below)
5. Click **Save**

---

## Employee Form - All Fields by Section

### Personal Details Section

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| First Name | Yes | Data | Employee's first name |
| Middle Name | No | Data | Employee's middle name |
| Last Name | No | Data | Employee's last name |
| Employee Name | Auto | Read Only | Full name (auto-generated) |
| Salutation | No | Select | Mr/Mrs/Ms/Dr |
| Gender | Yes | Select | Male/Female/Other |
| Date of Birth | No | Date | Birth date |
| Date of Joining | Yes | Date | Employment start date |
| Image | No | Attach Image | Profile photo |

#### How to Fill Personal Details
1. Enter **First Name** (required)
2. Enter **Middle Name** (optional)
3. Enter **Last Name** (optional)
4. Select **Salutation** from dropdown
5. Select **Gender** from dropdown
6. Click **Date of Birth** field → select date from calendar
7. Click **Date of Joining** field → select date (required)
8. Click **Image** → **Attach** → upload photo

### Company Details Section

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Status | Yes | Select | Active/Left/Suspended |
| Company | Yes | Link | Employing company |
| Department | No | Link | Employee's department |
| Designation | No | Link | Job title |
| Branch | No | Link | Office location |
| Employment Type | No | Link | Full-time/Part-time/Contract |
| Employee Grade | No | Link | Grade level |
| Reports To | No | Link | Direct manager |
| Employee Number | Auto | Data | Auto-generated ID |
| Naming Series | Yes | Select | ID prefix series |

#### How to Fill Company Details
1. Select **Status** (default: Active)
2. Select **Company** from dropdown (required)
3. Select **Department** from dropdown
4. Select **Designation** from dropdown
5. Select **Branch** from dropdown
6. Select **Employment Type** from dropdown
7. Select **Employee Grade** from dropdown
8. Select **Reports To** → search and select manager

### Singapore-Specific Fields Section

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| SG Residency Status | No | Select | Citizen/PR/Foreigner |
| SG Ethnicity | No | Select | Chinese/Malay/Indian/Others |
| NRIC/FIN | No | Data | National ID number |
| PR Start Date | No | Date | PR effective date (for CPF) |
| PR Year | Auto | Int | Years as PR (calculated) |

#### SG Residency Status Options
| Status | Description | CPF Applicable |
|--------|-------------|----------------|
| Singapore Citizen | Born or naturalized citizen | Full rates |
| Singapore PR | Permanent Resident | Graduated rates |
| Foreigner | Work permit/S Pass/EP holder | Not applicable |

#### SG Ethnicity Options
| Ethnicity | SHG Fund |
|-----------|----------|
| Chinese | CDAC |
| Malay | MBMF |
| Indian | SINDA |
| Others | ECF |

#### How to Fill Singapore Fields
1. Select **SG Residency Status** from dropdown
2. Select **SG Ethnicity** from dropdown
3. Enter **NRIC/FIN** number
4. If PR, click **PR Start Date** → select date
5. **PR Year** auto-calculates based on PR Start Date

### Contact Details Section

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Cell Number | No | Data | Mobile phone |
| Personal Email | No | Data | Personal email address |
| Company Email | No | Data | Work email address |
| Prefered Contact Email | No | Select | Company/Personal |
| Current Address | No | Small Text | Current residence |
| Permanent Address | No | Small Text | Permanent address |

#### How to Fill Contact Details
1. Enter **Cell Number**
2. Enter **Personal Email**
3. Enter **Company Email**
4. Select **Preferred Contact Email** (Company Email / Personal Email)
5. Enter **Current Address** in text area
6. Enter **Permanent Address** in text area
7. Check **Current Address Is** → **Permanent Address** if same

### Emergency Contact Section

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Emergency Contact Name | No | Data | Contact person name |
| Emergency Phone | No | Data | Contact phone number |
| Relation | No | Data | Relationship to employee |

#### How to Fill Emergency Contact
1. Enter **Emergency Contact Name**
2. Enter **Emergency Phone**
3. Enter **Relation** (e.g., Spouse, Parent, Sibling)

### Health Insurance Section

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Health Insurance Provider | No | Link | Insurance company |
| Health Insurance No | No | Data | Policy number |

#### How to Fill Health Insurance
1. Select **Health Insurance Provider** from dropdown
2. Enter **Health Insurance No**

### Attendance and Leave Details Section

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Attendance Device ID | No | Data | Biometric device ID |
| Holiday List | No | Link | Applicable holiday list |
| Default Shift | No | Link | Regular shift assignment |
| Leave Policy | No | Link | Assigned leave policy |

#### How to Fill Attendance/Leave Details
1. Enter **Attendance Device ID** (if using biometric)
2. Select **Holiday List** from dropdown
3. Select **Default Shift** from dropdown
4. Select **Leave Policy** from dropdown

### Salary Details Section

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Payroll Cost Center | No | Link | Cost center for payroll |
| Bank Name | No | Data | Employee's bank |
| Bank Account No | No | Data | Account number |
| IBAN | No | Data | International bank number |
| Mode of Payment | No | Link | Payment method |

#### How to Fill Salary Details
1. Select **Payroll Cost Center** from dropdown
2. Enter **Bank Name**
3. Enter **Bank Account No**
4. Enter **IBAN** (if applicable)
5. Select **Mode of Payment** (Bank Transfer/Cash/Cheque)

### Exit Section

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Relieving Date | No | Date | Last working day |
| Reason for Leaving | No | Data | Exit reason |
| Leave Encashed | No | Check | Leave balance encashed |
| Encashment Date | No | Date | Date of encashment |
| New Workplace | No | Data | Next employer (optional) |
| Feedback | No | Text | Exit feedback |

#### How to Fill Exit Details (When Employee Leaves)
1. Change **Status** to "Left"
2. Click **Relieving Date** → select last working day
3. Enter **Reason for Leaving**
4. Check **Leave Encashed** if applicable
5. Enter **Encashment Date**
6. Enter **New Workplace** (optional)
7. Enter **Feedback** from exit interview
8. Click **Save**

---

## Employee Lifecycle Overview

The employee lifecycle in HRDL8 covers the entire journey from hiring to exit:

| Stage | Document | URL |
|-------|----------|-----|
| Hiring | Job Offer | `/app/job-offer` |
| Onboarding | Employee Onboarding | `/app/employee-onboarding` |
| Active Employment | Employee | `/app/employee` |
| Promotion | Employee Promotion | `/app/employee-promotion` |
| Transfer | Employee Transfer | `/app/employee-transfer` |
| Separation | Employee Separation | `/app/employee-separation` |
| Exit | Full and Final Statement | `/app/full-and-final-statement` |

### How to View Employee Lifecycle
1. Open employee record (`/app/employee/{employee-id}`)
2. Click **Links** in the sidebar (right panel)
3. View linked documents:
   - Onboarding records
   - Promotions
   - Transfers
   - Leave applications
   - Attendance records
   - Salary slips

---

## Employee Skill Map

**URL:** `/app/employee-skill-map`

**Workspace:** HR

Employee Skill Map tracks skills and proficiency levels for employees.

### Skill Map Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Employee reference |
| Employee Name | Auto | Read Only | Auto-populated |
| Designation | Auto | Read Only | From employee |
| Skills | Yes | Table | List of skills |

### Skills Table Fields

| Field | Required | Description |
|-------|----------|-------------|
| Skill | Yes | Skill name (link to Skill doctype) |
| Proficiency | No | Rating (1-5 or percentage) |
| Evaluation Date | No | When skill was assessed |

### How to Create Employee Skill Map
1. Click **Sidebar** → **HR**
2. Click **Employee Skill Map** in shortcuts
3. Click **+ Add Employee Skill Map**
4. Select **Employee** from dropdown
5. In **Skills** table, click **Add Row**
6. Select **Skill** from dropdown
7. Enter **Proficiency** level
8. Enter **Evaluation Date**
9. Add more skills as needed
10. Click **Save**

### How to Create a Skill
1. Press `Ctrl + K` → type "Skill"
2. Click **+ Add Skill**
3. Enter **Skill Name** (e.g., "Python", "Project Management")
4. Click **Save**

---

## Employee Grade

**URL:** `/app/employee-grade`

**Workspace:** HR

Employee grades define levels within the organization and can auto-assign salary structures and leave policies.

### Grade Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Name | Yes | Data | Grade identifier |
| Default Salary Structure | No | Link | Auto-assign on employee creation |
| Default Leave Policy | No | Link | Auto-assign on employee creation |

### How to Create Employee Grade
1. Click **Sidebar** → **HR**
2. Click **Employee Grade** in shortcuts
3. Click **+ Add Employee Grade**
4. Enter **Name** (e.g., "L1 - Junior", "L2 - Associate")
5. Select **Default Salary Structure** (optional)
6. Select **Default Leave Policy** (optional)
7. Click **Save**

### How to Assign Grade to Employee
1. Open employee record
2. Scroll to **Company Details** section
3. Select **Employee Grade** from dropdown
4. Click **Save**

### Grade Benefits
- Automatic salary structure assignment
- Automatic leave policy assignment
- Reporting and analytics by grade
- Promotion tracking between grades

---

## Bulk Employee Operations

### How to Import Employees (Bulk Create)
1. Press `Ctrl + K` → type "Data Import"
2. Click **+ Add Data Import**
3. Select **Document Type** → "Employee"
4. Select **Import Type** → "Insert New Records"
5. Click **Download Template**
6. Fill the Excel template with employee data
7. Click **Attach** → upload filled template
8. Click **Start Import**
9. Review import log for errors

### How to Export Employee List
1. Go to `/app/employee`
2. Apply filters if needed
3. Click **Menu** (⋮) → **Export**
4. Select format (Excel/CSV)
5. Select fields to export
6. Click **Export**

---

## Quick Reference

### Employee Status Values
| Status | Description |
|--------|-------------|
| Active | Currently employed |
| Left | Employment ended |
| Suspended | Temporarily inactive |

### Required Fields Summary
- First Name
- Gender
- Date of Joining
- Company
- Status
- Naming Series

### Key URLs

| Document | URL |
|----------|-----|
| Employee List | `/app/employee` |
| New Employee | `/app/employee/new` |
| Employee Skill Map | `/app/employee-skill-map` |
| Employee Grade | `/app/employee-grade` |
| Skill | `/app/skill` |
| Data Import | `/app/data-import` |

### Employee Naming Series
| Series | Format | Example |
|--------|--------|---------|
| HR-EMP- | HR-EMP-##### | HR-EMP-00001 |
| EMP- | EMP-##### | EMP-00001 |
| Custom | As configured | HRDL8-001 |
