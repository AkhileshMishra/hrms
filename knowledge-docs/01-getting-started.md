# Getting Started with HRDL8

## Overview
HRDL8 is a comprehensive Human Resource Management System built on Frappe/ERPNext. This guide covers first login, dashboard navigation, and basic settings.

---

## First Login

**URL:** `https://d11okjnno7fxem.cloudfront.net`

### Steps to Login
1. Open your browser and navigate to `https://d11okjnno7fxem.cloudfront.net`
2. Enter your **Email** in the email field
3. Enter your **Password** in the password field
4. Click **Login** button
5. If first login, you may be prompted to change your password

### Forgot Password
1. Click **Forgot Password?** link on login page
2. Enter your registered email address
3. Click **Reset Password**
4. Check your email for reset link
5. Click the link and set a new password

---

## Dashboard Overview

After login, you land on the **Workspace** view. The dashboard provides quick access to all HR modules.

### Main Dashboard Elements

| Element | Description |
|---------|-------------|
| Sidebar | Left panel with all workspaces |
| Awesomebar | Top search bar (Ctrl+K) |
| Notifications | Bell icon for alerts |
| User Menu | Profile dropdown (top-right) |
| Workspace Content | Main area showing shortcuts and reports |

---

## Navigation Guide

### Sidebar Workspaces

HRDL8 has **10 main workspaces** accessible from the left sidebar:

| Workspace | Purpose | URL |
|-----------|---------|-----|
| HR | Core employee management | `/app/hr` |
| Leaves | Leave management | `/app/leaves` |
| Payroll | Salary processing | `/app/payroll` |
| Salary Payout | Payment disbursement | `/app/salary-payout` |
| Tax & Benefits | Tax declarations, benefits | `/app/tax-benefits` |
| Recruitment | Hiring workflow | `/app/recruitment` |
| Performance | Appraisals, goals | `/app/performance` |
| Shift & Attendance | Time tracking | `/app/shift-attendance` |
| Expense Claims | Expense reimbursement | `/app/expense-claims` |
| Employee Lifecycle | Onboarding to exit | `/app/employee-lifecycle` |

#### How to Navigate Workspaces
1. Look at the **left sidebar**
2. Click on any **workspace name** (e.g., HR, Leaves, Payroll)
3. The workspace opens showing shortcuts, reports, and dashboards

### Awesomebar (Global Search)

The Awesomebar is the fastest way to navigate HRDL8.

**Shortcut:** `Ctrl + K` (Windows/Linux) or `Cmd + K` (Mac)

#### How to Use Awesomebar
1. Press `Ctrl + K` or click the search bar at the top
2. Type what you're looking for:
   - Document type: `Employee`, `Leave Application`, `Salary Slip`
   - Document ID: `HR-EMP-00001`
   - Action: `New Employee`, `New Leave Application`
3. Press `Enter` or click the result

#### Awesomebar Search Examples

| Type This | Result |
|-----------|--------|
| `Employee` | Opens Employee list |
| `New Employee` | Opens new Employee form |
| `HR-EMP-00001` | Opens specific employee record |
| `Leave Application` | Opens Leave Application list |
| `Settings` | Shows settings options |

### Breadcrumbs

Breadcrumbs show your current location and allow quick navigation back.

**Location:** Top of the page, below the Awesomebar

#### Example Breadcrumb
`Home > HR > Employee > HR-EMP-00001`

#### How to Use Breadcrumbs
1. Look at the breadcrumb trail at the top
2. Click any item to navigate to that level
3. Click **Home** to return to the main workspace

### List View

List view displays all records of a document type in a table format.

**URL Pattern:** `/app/{doctype-hyphenated}`

#### List View Features

| Feature | Description | How to Access |
|---------|-------------|---------------|
| Filters | Filter records by field values | Click **Filters** button or filter icons |
| Sort | Sort by any column | Click column header |
| Search | Search within list | Use search box above list |
| Columns | Customize visible columns | Click **Edit Columns** |
| Export | Export to Excel/CSV | Menu → Export |
| Bulk Actions | Select multiple records | Check boxes → Actions dropdown |

#### How to Use List View
1. Navigate to any doctype (e.g., Sidebar → HR → Employee)
2. View all records in table format
3. Click **Filters** to add filter conditions
4. Click column headers to sort
5. Click any row to open the record
6. Use checkboxes for bulk selection

### Form View

Form view displays a single record with all its fields.

**URL Pattern:** `/app/{doctype-hyphenated}/{document-name}`

#### Form View Elements

| Element | Description |
|---------|-------------|
| Title | Document name/ID at top |
| Status | Workflow status indicator |
| Sections | Collapsible field groups |
| Timeline | Activity history on right |
| Actions | Save, Submit, Cancel buttons |
| Menu | Print, Email, Links, etc. |

#### How to Use Form View
1. Open any record from list view
2. Edit fields as needed
3. Click **Save** to save draft
4. Click **Submit** to finalize (if applicable)
5. Use **Menu** (⋮) for additional actions

### URL Patterns

Understanding URL patterns helps with direct navigation:

| Pattern | Example | Description |
|---------|---------|-------------|
| `/app/{doctype}` | `/app/employee` | List of all employees |
| `/app/{doctype}/new` | `/app/employee/new` | New employee form |
| `/app/{doctype}/{name}` | `/app/employee/HR-EMP-00001` | Specific employee |
| `/app/{workspace}` | `/app/hr` | Workspace view |

#### Common URLs Quick Reference

| Document | List URL | New Record URL |
|----------|----------|----------------|
| Employee | `/app/employee` | `/app/employee/new` |
| Leave Application | `/app/leave-application` | `/app/leave-application/new` |
| Attendance | `/app/attendance` | `/app/attendance/new` |
| Salary Slip | `/app/salary-slip` | `/app/salary-slip/new` |
| Expense Claim | `/app/expense-claim` | `/app/expense-claim/new` |

---

## User Profile Settings

### Accessing Your Profile
1. Click your **profile picture/avatar** in the top-right corner
2. Click **My Settings** or **Settings**
3. Your user profile form opens

**Direct URL:** `/app/user/{your-email}`

### Profile Settings Fields

| Section | Field | Description |
|---------|-------|-------------|
| **Basic** | First Name* | Your first name |
| | Last Name | Your last name |
| | Username | Login username |
| | Language | Interface language |
| | Time Zone | Your time zone |
| **Security** | New Password | Change password |
| | Logout All Sessions | Sign out everywhere |
| **Email** | Email Signature | Auto-signature for emails |
| | Send Me A Copy | CC yourself on sent emails |

*Required field

### How to Update Profile
1. Click **profile avatar** (top-right)
2. Click **My Settings**
3. Update desired fields:
   - Change **First Name** / **Last Name**
   - Select **Language** preference
   - Set **Time Zone**
4. Click **Save**

### How to Change Password
1. Click **profile avatar** (top-right)
2. Click **My Settings**
3. Scroll to **Change Password** section
4. Enter **New Password**
5. Re-enter in **Confirm Password** (if shown)
6. Click **Save**

### How to Set Email Signature
1. Click **profile avatar** (top-right)
2. Click **My Settings**
3. Scroll to **Email Settings** section
4. Enter your signature in **Email Signature** field
5. Click **Save**

---

## Quick Reference

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl + K` | Open Awesomebar |
| `Ctrl + S` | Save current document |
| `Ctrl + B` | Toggle sidebar |
| `Esc` | Close dialog/modal |
| `Ctrl + G` | Go to (quick navigation) |

### Getting Help
1. Click **Help** in the top menu (if available)
2. Use Awesomebar to search for documentation
3. Contact your HR administrator for access issues

### Common First Steps After Login
1. Update your profile information
2. Set your time zone
3. Explore the HR workspace
4. Check your assigned roles (visible in My Settings → Roles)

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Can't login | Check email/password, use Forgot Password |
| Page not loading | Clear browser cache, try incognito mode |
| Missing menu items | Check with admin about role permissions |
| Session expired | Re-login, check "Remember Me" option |
