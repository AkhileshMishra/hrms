# Admin Setup Guide

## Overview
This guide covers initial system configuration including company setup, user management, role assignment, and HR settings.

---

## Company Setup

**URL:** `/app/company`

**Workspace:** Settings

### Company Fields Reference

| Section | Field | Required | Description |
|---------|-------|----------|-------------|
| **Details** | Company Name | Yes | Legal company name |
| | Abbr | Yes | Short code (e.g., HRDL) |
| | Default Currency | Yes | Primary currency |
| | Country | Yes | Country of incorporation |
| | Domain | No | Business domain |
| **Address** | Address | No | Registered address |
| | City | No | City |
| | State | No | State/Province |
| | Pincode | No | Postal code |
| **Accounts** | Default Bank Account | No | Primary bank account |
| | Default Payroll Payable Account | No | For salary payables |
| | Default Expense Claim Payable Account | No | For expense payables |
| **HR** | Default Holiday List | No | Company-wide holidays |
| | Default Leave Policy | No | Standard leave policy |

### How to Create a Company
1. Click **Sidebar** → **Settings** (or use Awesomebar: `Ctrl + K` → type "Company")
2. Click **Company** in the shortcuts
3. Click **+ Add Company** button
4. Fill in required fields:
   - Enter **Company Name** (e.g., "HRDL8 Pte Ltd")
   - Enter **Abbr** (e.g., "HRDL8")
   - Select **Default Currency** (e.g., SGD)
   - Select **Country** (e.g., Singapore)
5. Fill optional fields as needed
6. Click **Save**

### How to Edit Company Settings
1. Press `Ctrl + K` → type "Company"
2. Click on your company name from the list
3. Edit desired fields
4. Click **Save**

---

## User Management

**URL:** `/app/user`

**Workspace:** Settings / Users

### User Fields Reference

| Section | Field | Required | Description |
|---------|-------|----------|-------------|
| **Basic** | Email | Yes | Login email (unique) |
| | First Name | Yes | User's first name |
| | Last Name | No | User's last name |
| | Username | No | Alternative login ID |
| | Language | No | Interface language |
| | Time Zone | No | User's time zone |
| **Password** | New Password | Yes* | Initial password |
| | Send Welcome Email | No | Email credentials to user |
| **Roles** | Role Profile | No | Predefined role set |
| | Roles | Yes | Individual role assignments |
| **Security** | Enabled | Yes | Account active status |
| | User Type | Yes | System User / Website User |

*Required for new users

### How to Create a New User
1. Press `Ctrl + K` → type "User"
2. Click **User** from results
3. Click **+ Add User** button
4. Fill in required fields:
   - Enter **Email** (e.g., john.doe@company.com)
   - Enter **First Name**
   - Enter **Last Name** (optional)
5. Set **New Password** or check **Send Welcome Email**
6. Scroll to **Roles** section
7. Check the roles to assign (see Roles section below)
8. Ensure **Enabled** is checked
9. Click **Save**

### How to Assign Roles to Existing User
1. Press `Ctrl + K` → type the user's email
2. Click on the user from results
3. Scroll to **Roles** section
4. Check/uncheck roles as needed
5. Click **Save**

---

## Roles Explained

HRDL8 has **10 primary roles** that control access to features:

| Role | Description | Key Permissions |
|------|-------------|-----------------|
| **Employee** | Basic employee access | View own records, apply leaves, submit expenses, view payslips |
| **HR User** | HR staff member | Create/edit employees, process leaves, manage attendance |
| **HR Manager** | Senior HR access | Full HR module access, approve workflows, access reports |
| **Leave Approver** | Approve leave requests | View team leaves, approve/reject leave applications |
| **Expense Approver** | Approve expenses | View team expenses, approve/reject expense claims |
| **Fleet Manager** | Vehicle management | Manage vehicles, vehicle logs, fleet reports |
| **Interviewer** | Recruitment interviews | View job applicants, submit interview feedback |
| **System Manager** | Full system access | All modules, settings, user management, configurations |
| **All** | Universal role | Basic access granted to all users |
| **Academics User** | Training/education | Training programs, certifications |

### Role Assignment Matrix

| Task | Employee | HR User | HR Manager | Leave Approver | Expense Approver |
|------|----------|---------|------------|----------------|------------------|
| View own profile | ✓ | ✓ | ✓ | ✓ | ✓ |
| Apply for leave | ✓ | ✓ | ✓ | ✓ | ✓ |
| Approve leaves | ✗ | ✗ | ✓ | ✓ | ✗ |
| Submit expenses | ✓ | ✓ | ✓ | ✓ | ✓ |
| Approve expenses | ✗ | ✗ | ✓ | ✗ | ✓ |
| Create employees | ✗ | ✓ | ✓ | ✗ | ✗ |
| Run payroll | ✗ | ✗ | ✓ | ✗ | ✗ |
| Access reports | ✗ | ✓ | ✓ | Limited | Limited |
| System settings | ✗ | ✗ | ✗ | ✗ | ✗ |

### How to Create a Role Profile (Predefined Role Set)
1. Press `Ctrl + K` → type "Role Profile"
2. Click **+ Add Role Profile**
3. Enter **Role Profile Name** (e.g., "HR Team Member")
4. In **Roles** table, click **Add Row**
5. Select roles to include
6. Click **Save**

### How to Assign Role Profile to User
1. Open the user record (`/app/user/{email}`)
2. In **Role Profile** field, select the profile
3. Click **Save**
4. Roles from the profile are automatically assigned

---

## HR Settings

**URL:** `/app/hr-settings`

**Workspace:** HR

HR Settings control global HR module behavior.

### How to Access HR Settings
1. Click **Sidebar** → **HR**
2. Click **HR Settings** in shortcuts
3. Or press `Ctrl + K` → type "HR Settings"

### HR Settings Sections

#### Employee Settings

| Field | Description | Default |
|-------|-------------|---------|
| Employee Naming By | How employee IDs are generated | Naming Series |
| Standard Working Hours | Daily work hours | 8 |
| Don't Send Emails | Disable HR email notifications | Unchecked |
| Retirement Age | Auto-calculate retirement date | 60 |

#### Leave Settings

| Field | Description | Default |
|-------|-------------|---------|
| Leave Approval Notification Template | Email template for approvals | - |
| Leave Status Notification Template | Email template for status updates | - |
| Show Leaves Of All Department Members | Visibility setting | Unchecked |
| Auto Leave Encashment | Auto-process leave encashment | Unchecked |

#### Hiring Settings

| Field | Description | Default |
|-------|-------------|---------|
| Check Vacancies On Job Offer Creation | Validate against staffing plan | Checked |
| Send Interview Reminder | Auto-remind interviewers | Checked |
| Remind Before (Hours) | Hours before interview | 24 |

#### Exit Settings

| Field | Description | Default |
|-------|-------------|---------|
| Exit Questionnaire Web Form | Link to exit survey | - |

### How to Configure HR Settings
1. Press `Ctrl + K` → type "HR Settings"
2. Click **HR Settings**
3. Configure each section:
   
   **Employee Settings:**
   - Set **Employee Naming By** (Naming Series / Employee Name / Field)
   - Enter **Standard Working Hours**
   - Set **Retirement Age**
   
   **Leave Settings:**
   - Select **Leave Approval Notification Template**
   - Select **Leave Status Notification Template**
   - Check/uncheck **Show Leaves Of All Department Members**
   
   **Hiring Settings:**
   - Check **Check Vacancies On Job Offer Creation**
   - Check **Send Interview Reminder**
   - Set **Remind Before** hours
   
4. Click **Save**

---

## Department Setup

**URL:** `/app/department`

**Workspace:** HR

### Department Fields

| Field | Required | Description |
|-------|----------|-------------|
| Department Name | Yes | Name of department |
| Company | Yes | Parent company |
| Parent Department | No | For hierarchy |
| Is Group | No | Has sub-departments |
| Disabled | No | Deactivate department |

### How to Create a Department
1. Click **Sidebar** → **HR**
2. Click **Department** in shortcuts
3. Click **+ Add Department**
4. Enter **Department Name** (e.g., "Engineering")
5. Select **Company**
6. Select **Parent Department** (if sub-department)
7. Click **Save**

### How to Create Department Hierarchy
1. Create parent department first (e.g., "Technology")
2. Check **Is Group** on parent
3. Save parent department
4. Create child department (e.g., "Frontend Team")
5. Select parent in **Parent Department** field
6. Save child department

---

## Designation Setup

**URL:** `/app/designation`

**Workspace:** HR

### Designation Fields

| Field | Required | Description |
|-------|----------|-------------|
| Designation Name | Yes | Job title |
| Description | No | Role description |

### How to Create a Designation
1. Click **Sidebar** → **HR**
2. Click **Designation** in shortcuts
3. Click **+ Add Designation**
4. Enter **Designation Name** (e.g., "Software Engineer")
5. Enter **Description** (optional)
6. Click **Save**

### Common Designations to Create
- CEO / Managing Director
- HR Manager / HR Executive
- Finance Manager / Accountant
- Software Engineer / Developer
- Sales Manager / Sales Executive
- Operations Manager

---

## Branch Setup

**URL:** `/app/branch`

**Workspace:** HR

### Branch Fields

| Field | Required | Description |
|-------|----------|-------------|
| Branch | Yes | Branch name/location |

### How to Create a Branch
1. Click **Sidebar** → **HR**
2. Click **Branch** in shortcuts
3. Click **+ Add Branch**
4. Enter **Branch** name (e.g., "Singapore HQ")
5. Click **Save**

---

## Employment Type Setup

**URL:** `/app/employment-type`

**Workspace:** HR

### Employment Type Fields

| Field | Required | Description |
|-------|----------|-------------|
| Employment Type Name | Yes | Type of employment |

### How to Create Employment Type
1. Click **Sidebar** → **HR**
2. Click **Employment Type** in shortcuts
3. Click **+ Add Employment Type**
4. Enter **Employment Type Name**
5. Click **Save**

### Standard Employment Types
| Type | Description |
|------|-------------|
| Full-time | Regular full-time employee |
| Part-time | Part-time employee |
| Contract | Fixed-term contract |
| Intern | Internship position |
| Probation | Probationary period |
| Consultant | External consultant |

---

## Employee Grade Setup

**URL:** `/app/employee-grade`

**Workspace:** HR

### Employee Grade Fields

| Field | Required | Description |
|-------|----------|-------------|
| Name | Yes | Grade identifier |
| Default Salary Structure | No | Auto-assign salary structure |
| Default Leave Policy | No | Auto-assign leave policy |

### How to Create Employee Grade
1. Click **Sidebar** → **HR**
2. Click **Employee Grade** in shortcuts
3. Click **+ Add Employee Grade**
4. Enter **Name** (e.g., "Grade A", "L1", "Senior")
5. Select **Default Salary Structure** (optional)
6. Select **Default Leave Policy** (optional)
7. Click **Save**

### Sample Grade Structure
| Grade | Level | Typical Roles |
|-------|-------|---------------|
| L1 | Entry | Junior staff, Interns |
| L2 | Associate | Associates, Executives |
| L3 | Senior | Senior staff, Specialists |
| L4 | Lead | Team leads, Supervisors |
| L5 | Manager | Managers |
| L6 | Director | Directors, VPs |
| L7 | Executive | C-suite |

---

## Quick Reference

### Admin Setup Checklist
- [ ] Create Company
- [ ] Configure HR Settings
- [ ] Create Departments
- [ ] Create Designations
- [ ] Create Branches
- [ ] Create Employment Types
- [ ] Create Employee Grades
- [ ] Create Users
- [ ] Assign Roles

### Key URLs

| Document | URL |
|----------|-----|
| Company | `/app/company` |
| User | `/app/user` |
| HR Settings | `/app/hr-settings` |
| Department | `/app/department` |
| Designation | `/app/designation` |
| Branch | `/app/branch` |
| Employment Type | `/app/employment-type` |
| Employee Grade | `/app/employee-grade` |
| Role Profile | `/app/role-profile` |

### Minimum Required Setup
1. At least one **Company**
2. At least one **Department**
3. At least one **Designation**
4. **HR Settings** configured
5. **Users** created with appropriate **Roles**
