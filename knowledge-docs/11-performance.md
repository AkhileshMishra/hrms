# Performance Management

## Overview
This guide covers performance appraisals, goal setting, feedback, promotions, and performance analytics.

---

## Appraisal Template

**URL:** `/app/appraisal-template`

**Workspace:** Performance

Appraisal Template defines the structure and criteria for performance evaluations.

### Appraisal Template Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Template Name | Yes | Data | Template identifier |
| Description | No | Text | Template description |
| Goals | Yes | Table | KRA/Goal categories |

### Goals Table (KRA)

| Field | Required | Description |
|-------|----------|-------------|
| KRA | Yes | Key Result Area name |
| Per Weightage | Yes | Weight percentage |

### How to Create Appraisal Template
1. Click **Sidebar** → **Performance**
2. Click **Appraisal Template** in shortcuts
3. Click **+ Add Appraisal Template**
4. Enter **Template Name** (e.g., "Engineering Appraisal")
5. Enter **Description** (optional)
6. In **Goals** table:
   - Click **Add Row**
   - Enter **KRA** (e.g., "Technical Skills")
   - Enter **Per Weightage** (e.g., 30)
   - Repeat for each KRA
7. Ensure total weightage = 100%
8. Click **Save**

### Sample KRA Structure

| KRA | Weightage |
|-----|-----------|
| Technical Skills | 30% |
| Project Delivery | 25% |
| Communication | 15% |
| Teamwork | 15% |
| Innovation | 15% |
| **Total** | **100%** |

---

## Appraisal Cycle

**URL:** `/app/appraisal-cycle`

**Workspace:** Performance

Appraisal Cycle manages the performance review period and creates appraisals for employees.

### Appraisal Cycle Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Appraisal Cycle Name | Yes | Data | Cycle identifier |
| Company | Yes | Link | Company |
| Start Date | Yes | Date | Cycle start |
| End Date | Yes | Date | Cycle end |
| Appraisal Template | Yes | Link | Template to use |
| KRA Evaluation Method | No | Select | Manual/Automated |
| Calculate Final Score Based On | No | Select | Average/Sum |
| Employees | No | Table | Employees in cycle |

### Appraisal Cycle Workflow

1. **Create Cycle** - Define period and template
2. **Get Employees** - Fetch eligible employees
3. **Create Appraisals** - Generate individual appraisals
4. **Self Appraisal** - Employees rate themselves
5. **Manager Appraisal** - Managers rate employees
6. **Final Review** - HR reviews and finalizes

### How to Create Appraisal Cycle
1. Click **Sidebar** → **Performance**
2. Click **Appraisal Cycle** in shortcuts
3. Click **+ Add Appraisal Cycle**
4. Enter **Appraisal Cycle Name** (e.g., "2024 Annual Review")
5. Select **Company**
6. Select **Start Date**
7. Select **End Date**
8. Select **Appraisal Template**
9. Select **KRA Evaluation Method**:
   - Manual: Managers enter scores
   - Automated: Based on goals
10. Select **Calculate Final Score Based On**
11. Click **Save**

### How to Get Employees for Appraisal Cycle
1. Open the appraisal cycle
2. Click **Get Employees** button
3. Filter by (optional):
   - Department
   - Designation
   - Branch
4. Click **Get Employees**
5. Review **Employees** table
6. Remove any employees if needed
7. Click **Save**

### How to Create Appraisals from Cycle
1. Open the appraisal cycle (with employees)
2. Click **Create Appraisals** button
3. System creates individual appraisal records
4. Status shows "Appraisals Created"
5. Click **View Appraisals** to see list

---

## Appraisal

**URL:** `/app/appraisal`

**Workspace:** Performance

Appraisal is the individual performance review document for each employee.

### Appraisal Fields

| Section | Field | Required | Description |
|---------|-------|----------|-------------|
| **Basic** | Employee | Yes | Employee reference |
| | Appraisal Cycle | No | Parent cycle |
| | Appraisal Template | Yes | Template used |
| | Start Date | Yes | Review period start |
| | End Date | Yes | Review period end |
| | Status | Yes | Draft/Submitted/Completed |
| **Self Appraisal** | Self Score | Auto | Employee's self rating |
| | Appraisal KRA | Yes | Table of KRA ratings |
| **Manager Appraisal** | Appraiser | No | Reviewing manager |
| | Final Score | Auto | Manager's rating |
| **Feedback** | Feedback | No | Table of feedback |
| **Goals** | Goals | No | Linked goals |

### Appraisal KRA Table

| Field | Required | Description |
|-------|----------|-------------|
| KRA | Yes | Key Result Area |
| Weightage | Yes | Weight percentage |
| Self Score | No | Employee's rating (1-5) |
| Score | No | Manager's rating (1-5) |
| Score Earned | Auto | Weighted score |

### How to Complete Self Appraisal (Employee)
1. Click **Sidebar** → **Performance**
2. Click **Appraisal** in shortcuts
3. Filter by **Employee** → your name
4. Open your appraisal
5. In **Appraisal KRA** table:
   - For each KRA, enter **Self Score** (1-5)
   - Add comments if needed
6. Review **Self Score** (auto-calculated)
7. Click **Save**
8. Click **Submit** (sends to manager)

### How to Complete Manager Appraisal (Manager)
1. Click **Sidebar** → **Performance**
2. Click **Appraisal** in shortcuts
3. Filter by **Appraiser** → your name
4. Filter by **Status** → "Submitted"
5. Open the appraisal
6. Review employee's self scores
7. In **Appraisal KRA** table:
   - For each KRA, enter **Score** (1-5)
8. Review **Final Score** (auto-calculated)
9. Add **Feedback** in feedback table
10. Click **Save**
11. Click **Complete** to finalize

### Appraisal Rating Scale

| Score | Rating | Description |
|-------|--------|-------------|
| 5 | Exceptional | Consistently exceeds expectations |
| 4 | Exceeds | Often exceeds expectations |
| 3 | Meets | Meets expectations |
| 2 | Below | Sometimes meets expectations |
| 1 | Unsatisfactory | Does not meet expectations |

---

## Goal

**URL:** `/app/goal`

**Workspace:** Performance

Goal tracks individual and team objectives with progress monitoring.

### Goal Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Goal Name | Yes | Data | Goal title |
| Employee | Yes | Link | Goal owner |
| KRA | No | Link | Related KRA |
| Appraisal Cycle | No | Link | Related cycle |
| Status | Yes | Select | Pending/In Progress/Completed |
| Progress | No | Percent | Completion percentage |
| Is Group Goal | No | Check | Team goal |
| Parent Goal | No | Link | For hierarchy |
| Start Date | No | Date | Goal start |
| End Date | No | Date | Goal deadline |
| Description | No | Text | Goal details |

### Goal Status Options

| Status | Description |
|--------|-------------|
| Pending | Not started |
| In Progress | Currently working |
| Completed | Achieved |
| Archived | No longer relevant |

### How to Create Goal (Employee)
1. Click **Sidebar** → **Performance**
2. Click **Goal** in shortcuts
3. Click **+ Add Goal**
4. Enter **Goal Name** (e.g., "Complete AWS Certification")
5. **Employee** auto-fills
6. Select **KRA** (if linked to appraisal)
7. Select **Appraisal Cycle** (if applicable)
8. Select **Status** → "Pending"
9. Enter **Progress** (0%)
10. Select **Start Date**
11. Select **End Date**
12. Enter **Description**
13. Click **Save**

### How to Create Goal Hierarchy (Tree Structure)
1. Create parent goal first (e.g., "Q1 Objectives")
2. Check **Is Group Goal** on parent
3. Save parent goal
4. Create child goal (e.g., "Complete Project A")
5. Select **Parent Goal** → parent goal name
6. Save child goal
7. View hierarchy in Goal tree view

### How to Update Goal Progress
1. Open the goal
2. Update **Progress** percentage
3. Update **Status** if needed
4. Add notes in description
5. Click **Save**

### How to View Goal Tree
1. Click **Sidebar** → **Performance**
2. Click **Goal** in shortcuts
3. Click **Tree View** toggle (if available)
4. Or filter by **Parent Goal** to see hierarchy

---

## Employee Performance Feedback

**URL:** `/app/employee-performance-feedback`

**Workspace:** Performance

Employee Performance Feedback captures ongoing feedback outside formal appraisals.

### Feedback Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Feedback recipient |
| Reviewer | Yes | Link | Feedback giver |
| Company | Yes | Link | Company |
| Feedback | Yes | Text | Feedback content |
| Feedback Rating | No | Select | Positive/Neutral/Negative |

### How to Give Performance Feedback
1. Click **Sidebar** → **Performance**
2. Click **Employee Performance Feedback** in shortcuts
3. Click **+ Add Employee Performance Feedback**
4. Select **Employee** (feedback recipient)
5. **Reviewer** auto-fills with your name
6. Select **Company**
7. Enter **Feedback** (detailed comments)
8. Select **Feedback Rating**:
   - Positive
   - Neutral
   - Negative
9. Click **Save**
10. Click **Submit**

### How to View Feedback Received (Employee)
1. Click **Sidebar** → **Performance**
2. Click **Employee Performance Feedback**
3. Filter by **Employee** → your name
4. View all feedback received

---

## Employee Promotion

**URL:** `/app/employee-promotion`

**Workspace:** Performance / Employee Lifecycle

Employee Promotion records grade/designation changes based on performance.

### Promotion Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Employee | Yes | Link | Employee reference |
| Company | Yes | Link | Company |
| Promotion Date | Yes | Date | Effective date |
| Promotion Details | Yes | Table | Changes |

### Promotion Details Table

| Field | Required | Description |
|-------|----------|-------------|
| Property | Yes | Field to change |
| Current | Auto | Current value |
| New | Yes | New value |

### How to Create Employee Promotion
1. Click **Sidebar** → **Performance**
2. Click **Employee Promotion** in shortcuts
3. Click **+ Add Employee Promotion**
4. Select **Employee**
5. Select **Company**
6. Select **Promotion Date**
7. In **Promotion Details** table:
   - Click **Add Row**
   - Select **Property** (e.g., "Designation")
   - **Current** auto-fills
   - Select **New** value
   - Add more rows for other changes (Grade, Department, etc.)
8. Click **Save**
9. Click **Submit**
10. Employee record updates automatically

### Common Promotion Properties

| Property | Description |
|----------|-------------|
| Designation | Job title change |
| Employee Grade | Grade level change |
| Department | Department transfer |
| Branch | Location change |

---

## Appraisal Overview Report

**URL:** `/app/query-report/Appraisal Overview`

**Workspace:** Performance

### How to View Appraisal Overview
1. Click **Sidebar** → **Performance**
2. Click **Appraisal Overview** in Reports
3. Select **Company**
4. Select **Appraisal Cycle**
5. View summary:
   - Appraisals by status
   - Score distribution
   - Department averages

### Other Performance Reports

| Report | URL | Description |
|--------|-----|-------------|
| Appraisal Overview | `/app/query-report/Appraisal Overview` | Cycle summary |
| Goal Progress | `/app/query-report/Goal Progress` | Goal completion |

---

## Quick Reference

### Appraisal Workflow
```
Create Template → Create Cycle → Get Employees → Create Appraisals → Self Appraisal → Manager Appraisal → Complete
```

### Appraisal Status Flow
```
Draft → Submitted (by employee) → Completed (by manager)
```

### Key URLs

| Document | URL |
|----------|-----|
| Appraisal Template | `/app/appraisal-template` |
| Appraisal Cycle | `/app/appraisal-cycle` |
| Appraisal | `/app/appraisal` |
| Goal | `/app/goal` |
| Employee Performance Feedback | `/app/employee-performance-feedback` |
| Employee Promotion | `/app/employee-promotion` |

### Performance Setup Checklist
- [ ] Create Appraisal Templates with KRAs
- [ ] Create Appraisal Cycle
- [ ] Add employees to cycle
- [ ] Create appraisals
- [ ] Communicate timeline to employees
- [ ] Monitor completion

### Required Roles
| Action | Required Role |
|--------|---------------|
| Complete self appraisal | Employee |
| Complete manager appraisal | HR Manager, Reports To |
| Create appraisal cycle | HR Manager |
| Create goals | Employee |
| Give feedback | Employee, HR User |
| Process promotion | HR Manager |

### Rating Guidelines

| Score | Criteria |
|-------|----------|
| 5 | Top 10% performer, exceptional results |
| 4 | Above average, exceeds most goals |
| 3 | Solid performer, meets all expectations |
| 2 | Needs improvement in some areas |
| 1 | Significant improvement required |
