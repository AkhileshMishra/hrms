# Attendance & Shift Management

## Overview
This guide covers attendance tracking, shift management, employee check-ins, and related reports.

---

## Manual Attendance

**URL:** `/app/attendance`

**Workspace:** Shift & Attendance

### Attendance Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Employee reference |
| Attendance Date | Yes | Date | Date of attendance |
| Status | Yes | Select | Present/Absent/On Leave/Half Day/Work From Home |
| Shift | No | Link | Assigned shift |
| In Time | No | Time | Check-in time |
| Out Time | No | Time | Check-out time |
| Working Hours | Auto | Float | Calculated hours |
| Late Entry | No | Check | Marked late |
| Early Exit | No | Check | Left early |

### Attendance Status Options

| Status | Description |
|--------|-------------|
| Present | Full day attendance |
| Absent | Did not attend |
| On Leave | On approved leave |
| Half Day | Partial attendance |
| Work From Home | Remote work |

### How to Mark Manual Attendance
1. Click **Sidebar** → **Shift & Attendance**
2. Click **Attendance** in shortcuts
3. Click **+ Add Attendance**
4. Select **Employee** from dropdown
5. Select **Attendance Date**
6. Select **Status** (Present/Absent/etc.)
7. Select **Shift** (if applicable)
8. Enter **In Time** (optional)
9. Enter **Out Time** (optional)
10. Check **Late Entry** or **Early Exit** if applicable
11. Click **Save**
12. Click **Submit**

---

## Attendance Request

**URL:** `/app/attendance-request`

**Workspace:** Shift & Attendance

Attendance Request allows employees to request attendance corrections or work-from-home.

### Attendance Request Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Employee reference |
| From Date | Yes | Date | Request start date |
| To Date | Yes | Date | Request end date |
| Reason | Yes | Select | Work From Home/On Duty/Attendance Correction |
| Explanation | No | Text | Additional details |
| Half Day | No | Check | Half day request |
| Half Day Date | Cond | Date | Which day is half |

### How to Submit Attendance Request (Employee)
1. Click **Sidebar** → **Shift & Attendance**
2. Click **Attendance Request** in shortcuts
3. Click **+ Add Attendance Request**
4. **Employee** auto-fills with your name
5. Select **From Date**
6. Select **To Date**
7. Select **Reason**:
   - Work From Home
   - On Duty
   - Attendance Correction
8. Enter **Explanation**
9. Check **Half Day** if applicable
10. Click **Save**
11. Click **Submit**

### How to Approve Attendance Request (Manager)
1. Click **Sidebar** → **Shift & Attendance**
2. Click **Attendance Request** in shortcuts
3. Filter by **Status** → "Open"
4. Open the request
5. Review details
6. Click **Approve** or **Reject**

---

## Employee Checkin

**URL:** `/app/employee-checkin`

**Workspace:** Shift & Attendance

Employee Checkin records clock-in/clock-out with optional geolocation.

### Employee Checkin Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Employee reference |
| Time | Yes | Datetime | Check-in/out timestamp |
| Log Type | Yes | Select | IN/OUT |
| Device ID | No | Data | Biometric device ID |
| Latitude | No | Float | GPS latitude |
| Longitude | No | Float | GPS longitude |
| Location | No | Data | Location name |

### How to Record Employee Checkin (Manual)
1. Click **Sidebar** → **Shift & Attendance**
2. Click **Employee Checkin** in shortcuts
3. Click **+ Add Employee Checkin**
4. Select **Employee**
5. Select **Time** (date and time)
6. Select **Log Type** (IN or OUT)
7. Enter **Device ID** (optional)
8. Enter **Latitude** and **Longitude** (optional)
9. Click **Save**

### Geolocation Checkin
When using mobile or web checkin with geolocation:
1. Employee opens checkin interface
2. Browser requests location permission
3. Employee clicks **Check In** or **Check Out**
4. System records:
   - Current timestamp
   - GPS coordinates (Latitude/Longitude)
   - Log type (IN/OUT)

---

## Employee Attendance Tool (Bulk)

**URL:** `/app/employee-attendance-tool`

**Workspace:** Shift & Attendance

Employee Attendance Tool allows marking attendance for multiple employees at once.

### How to Use Employee Attendance Tool
1. Click **Sidebar** → **Shift & Attendance**
2. Click **Employee Attendance Tool** in shortcuts
3. Select **Attendance Date**
4. Select **Company**
5. Optionally filter by:
   - **Department**
   - **Branch**
   - **Designation**
6. Click **Get Employees**
7. Employee list loads with checkboxes
8. For each employee, select **Status**:
   - Present
   - Absent
   - Half Day
   - Work From Home
9. Check employees to mark
10. Click **Mark Attendance**
11. Attendance records are created for selected employees

### Bulk Mark All Present
1. Follow steps 1-6 above
2. Click **Check All** to select all employees
3. Ensure **Status** is "Present"
4. Click **Mark Attendance**

---

## Upload Attendance (CSV)

**URL:** `/app/upload-attendance`

**Workspace:** Shift & Attendance

Upload Attendance allows importing attendance data from CSV files.

### CSV Format Requirements

| Column | Required | Format | Description |
|--------|----------|--------|-------------|
| Employee | Yes | Employee ID | e.g., HR-EMP-00001 |
| Attendance Date | Yes | YYYY-MM-DD | Date of attendance |
| Status | Yes | Text | Present/Absent/Half Day/On Leave |
| In Time | No | HH:MM:SS | Check-in time |
| Out Time | No | HH:MM:SS | Check-out time |

### Sample CSV
```csv
Employee,Attendance Date,Status,In Time,Out Time
HR-EMP-00001,2024-01-15,Present,09:00:00,18:00:00
HR-EMP-00002,2024-01-15,Present,09:15:00,18:30:00
HR-EMP-00003,2024-01-15,Absent,,
```

### How to Upload Attendance
1. Click **Sidebar** → **Shift & Attendance**
2. Click **Upload Attendance** in shortcuts
3. Click **Download Template** to get CSV format
4. Fill the template with attendance data
5. Click **Attach** → select your CSV file
6. Click **Upload**
7. Review import summary
8. Fix any errors and re-upload if needed

---

## Shift Type Setup

**URL:** `/app/shift-type`

**Workspace:** Shift & Attendance

Shift Type defines work schedules with timing and rules.

### Shift Type Fields

| Section | Field | Required | Description |
|---------|-------|----------|-------------|
| **Basic** | Shift Name | Yes | Shift identifier |
| | Start Time | Yes | Shift start time |
| | End Time | Yes | Shift end time |
| | Holiday List | No | Applicable holidays |
| **Working Hours** | Working Hours Calculation Based On | No | First/Last Checkin |
| | Working Hours Threshold For Half Day | No | Hours for half day |
| | Working Hours Threshold For Absent | No | Hours for absent |
| **Late Entry/Early Exit** | Enable Entry Grace Period | No | Allow late buffer |
| | Late Entry Grace Period | No | Minutes allowed late |
| | Enable Exit Grace Period | No | Allow early exit buffer |
| | Early Exit Grace Period | No | Minutes allowed early |
| **Auto Attendance** | Enable Auto Attendance | No | Auto-mark from checkins |
| | Process Attendance After | No | Minutes after shift end |
| | Last Sync of Checkin | Auto | Last processed time |

### How to Create a Shift Type
1. Click **Sidebar** → **Shift & Attendance**
2. Click **Shift Type** in shortcuts
3. Click **+ Add Shift Type**
4. Enter **Shift Name** (e.g., "Day Shift", "Night Shift")
5. Enter **Start Time** (e.g., 09:00)
6. Enter **End Time** (e.g., 18:00)
7. Select **Holiday List**

   **Configure Working Hours:**
8. Select **Working Hours Calculation Based On**
9. Enter **Working Hours Threshold For Half Day** (e.g., 4)
10. Enter **Working Hours Threshold For Absent** (e.g., 2)

    **Configure Grace Periods:**
11. Check **Enable Entry Grace Period**
12. Enter **Late Entry Grace Period** (e.g., 15 minutes)
13. Check **Enable Exit Grace Period**
14. Enter **Early Exit Grace Period** (e.g., 15 minutes)

    **Configure Auto Attendance:**
15. Check **Enable Auto Attendance**
16. Enter **Process Attendance After** (e.g., 60 minutes)
17. Click **Save**

### Common Shift Configurations

| Shift Name | Start | End | Grace Period |
|------------|-------|-----|--------------|
| Day Shift | 09:00 | 18:00 | 15 min |
| Morning Shift | 06:00 | 14:00 | 10 min |
| Evening Shift | 14:00 | 22:00 | 10 min |
| Night Shift | 22:00 | 06:00 | 15 min |
| Flexible | 08:00 | 20:00 | 60 min |

---

## Shift Assignment

**URL:** `/app/shift-assignment`

**Workspace:** Shift & Attendance

Shift Assignment assigns shifts to employees for specific periods.

### Shift Assignment Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Employee reference |
| Shift Type | Yes | Link | Shift to assign |
| Company | Yes | Link | Company |
| Start Date | Yes | Date | Assignment start |
| End Date | No | Date | Assignment end (blank = ongoing) |
| Status | Yes | Select | Active/Inactive |

### How to Assign Shift to Employee
1. Click **Sidebar** → **Shift & Attendance**
2. Click **Shift Assignment** in shortcuts
3. Click **+ Add Shift Assignment**
4. Select **Employee**
5. Select **Shift Type**
6. Select **Company**
7. Select **Start Date**
8. Select **End Date** (leave blank for ongoing)
9. **Status** defaults to Active
10. Click **Save**
11. Click **Submit**

### How to Bulk Assign Shifts
1. Click **Sidebar** → **Shift & Attendance**
2. Click **Shift Assignment** in shortcuts
3. Click **Menu** (⋮) → **Assign Shift**
4. Select **Shift Type**
5. Select **Company**
6. Select **Start Date** and **End Date**
7. Filter employees by:
   - Department
   - Designation
   - Branch
8. Click **Get Employees**
9. Check employees to assign
10. Click **Assign**

---

## Shift Request

**URL:** `/app/shift-request`

**Workspace:** Shift & Attendance

Shift Request allows employees to request shift changes.

### Shift Request Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Employee reference |
| Shift Type | Yes | Link | Requested shift |
| From Date | Yes | Date | Request start date |
| To Date | Yes | Date | Request end date |
| Approver | Yes | Link | Approving manager |
| Reason | No | Text | Request reason |

### How to Request Shift Change (Employee)
1. Click **Sidebar** → **Shift & Attendance**
2. Click **Shift Request** in shortcuts
3. Click **+ Add Shift Request**
4. **Employee** auto-fills
5. Select **Shift Type** (desired shift)
6. Select **From Date**
7. Select **To Date**
8. **Approver** auto-fills based on Reports To
9. Enter **Reason**
10. Click **Save**
11. Click **Submit**

### How to Approve Shift Request (Manager)
1. Click **Sidebar** → **Shift & Attendance**
2. Click **Shift Request** in shortcuts
3. Filter by **Status** → "Draft" or "Pending"
4. Open the request
5. Review details
6. Click **Approve** or **Reject**
7. If approved, Shift Assignment is auto-created

---

## Shift Schedule

**URL:** `/app/shift-schedule`

**Workspace:** Shift & Attendance

Shift Schedule provides a calendar view of shift assignments.

### How to View Shift Schedule
1. Click **Sidebar** → **Shift & Attendance**
2. Click **Shift Schedule** in shortcuts
3. Select **Company**
4. Select **Department** (optional)
5. Select date range
6. View calendar with shift assignments
7. Click on any cell to see details

---

## Attendance Reports

**Workspace:** Shift & Attendance

### Available Reports

| Report | URL | Description |
|--------|-----|-------------|
| Monthly Attendance Sheet | `/app/query-report/Monthly Attendance Sheet` | Monthly attendance grid |
| Employee Attendance Summary | `/app/query-report/Employee Attendance Summary` | Summary by employee |
| Shift Attendance | `/app/query-report/Shift Attendance` | Attendance by shift |

### How to View Monthly Attendance Sheet
1. Click **Sidebar** → **Shift & Attendance**
2. Click **Monthly Attendance Sheet** in Reports
3. Select **Year**
4. Select **Month**
5. Select **Company**
6. Optionally filter by **Department**, **Branch**
7. View attendance grid with daily status

### How to View Employee Attendance Summary
1. Click **Sidebar** → **Shift & Attendance**
2. Click **Employee Attendance Summary** in Reports
3. Select **From Date** and **To Date**
4. Select **Company**
5. View summary:
   - Total Present
   - Total Absent
   - Total Leave
   - Total Late

### How to Export Attendance Report
1. Open any attendance report
2. Click **Menu** (⋮) → **Export**
3. Select format (Excel/CSV)
4. Click **Export**

---

## Quick Reference

### Attendance Status Values
| Status | Code | Description |
|--------|------|-------------|
| Present | P | Full attendance |
| Absent | A | No attendance |
| Half Day | HD | Partial attendance |
| On Leave | L | Approved leave |
| Work From Home | WFH | Remote work |

### Key URLs

| Document | URL |
|----------|-----|
| Attendance | `/app/attendance` |
| Attendance Request | `/app/attendance-request` |
| Employee Checkin | `/app/employee-checkin` |
| Employee Attendance Tool | `/app/employee-attendance-tool` |
| Upload Attendance | `/app/upload-attendance` |
| Shift Type | `/app/shift-type` |
| Shift Assignment | `/app/shift-assignment` |
| Shift Request | `/app/shift-request` |

### Attendance Setup Checklist
- [ ] Create Shift Types
- [ ] Assign Shifts to Employees
- [ ] Configure Auto Attendance (if using checkins)
- [ ] Set up Holiday List
- [ ] Test attendance marking

### Required Roles
| Action | Required Role |
|--------|---------------|
| Mark own attendance | Employee |
| Mark others' attendance | HR User, HR Manager |
| Approve attendance requests | HR Manager, Reports To |
| Create shift types | HR Manager |
| Assign shifts | HR User, HR Manager |
