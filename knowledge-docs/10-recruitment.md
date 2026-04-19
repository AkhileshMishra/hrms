# Recruitment Management

## Overview
This guide covers the complete recruitment workflow from staffing plans to job offers, including interviews, applicant tracking, and analytics.

---

## Staffing Plan

**URL:** `/app/staffing-plan`

**Workspace:** Recruitment

Staffing Plan defines hiring needs for departments over a period.

### Staffing Plan Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Name | Yes | Data | Plan identifier |
| Company | Yes | Link | Company |
| From Date | Yes | Date | Plan start |
| To Date | Yes | Date | Plan end |
| Staffing Plan Details | Yes | Table | Position requirements |
| Total Estimated Budget | Auto | Currency | Sum of budgets |

### Staffing Plan Details Table

| Field | Required | Description |
|-------|----------|-------------|
| Designation | Yes | Job title |
| Department | No | Target department |
| Vacancies | Yes | Number of positions |
| Current Count | Auto | Existing employees |
| Current Openings | Auto | Active job openings |
| Estimated Cost Per Position | No | Budget per hire |
| Total Estimated Cost | Auto | Vacancies × Cost |

### How to Create Staffing Plan
1. Click **Sidebar** → **Recruitment**
2. Click **Staffing Plan** in shortcuts
3. Click **+ Add Staffing Plan**
4. Enter **Name** (e.g., "Q1 2024 Hiring Plan")
5. Select **Company**
6. Select **From Date**
7. Select **To Date**
8. In **Staffing Plan Details** table:
   - Click **Add Row**
   - Select **Designation** (e.g., "Software Engineer")
   - Select **Department** (e.g., "Engineering")
   - Enter **Vacancies** (e.g., 5)
   - Enter **Estimated Cost Per Position** (optional)
   - Repeat for each position
9. Review **Total Estimated Budget**
10. Click **Save**
11. Click **Submit**

---

## Job Requisition

**URL:** `/app/job-requisition`

**Workspace:** Recruitment

Job Requisition is a formal request to fill a position, linked to staffing plans.

### Job Requisition Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Job Title | Yes | Data | Position title |
| Department | Yes | Link | Hiring department |
| Designation | Yes | Link | Job designation |
| Staffing Plan | No | Link | Related staffing plan |
| Requested By | Yes | Link | Requesting manager |
| No of Positions | Yes | Int | Positions to fill |
| Expected Compensation | No | Currency | Salary budget |
| Description | No | Text | Job details |
| Reason for Requesting | No | Text | Business justification |

### How to Create Job Requisition
1. Click **Sidebar** → **Recruitment**
2. Click **Job Requisition** in shortcuts
3. Click **+ Add Job Requisition**
4. Enter **Job Title**
5. Select **Department**
6. Select **Designation**
7. Select **Staffing Plan** (if applicable)
8. Select **Requested By** (manager)
9. Enter **No of Positions**
10. Enter **Expected Compensation**
11. Enter **Description**
12. Enter **Reason for Requesting**
13. Click **Save**
14. Click **Submit**

### How to Approve Job Requisition
1. Click **Sidebar** → **Recruitment**
2. Click **Job Requisition**
3. Filter by **Status** → "Pending Approval"
4. Open the requisition
5. Review details
6. Click **Approve** or **Reject**

---

## Job Opening

**URL:** `/app/job-opening`

**Workspace:** Recruitment

Job Opening is a published position that candidates can apply for.

### Job Opening Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Job Title | Yes | Data | Position title |
| Company | Yes | Link | Hiring company |
| Designation | Yes | Link | Job designation |
| Department | No | Link | Department |
| Status | Yes | Select | Open/Closed |
| Staffing Plan | No | Link | Related plan |
| Planned Vacancies | Auto | Int | From staffing plan |
| Vacancies | No | Int | Positions available |
| Posted On | No | Date | Publication date |
| Closes On | No | Date | Application deadline |
| Description | No | Text | Job description |
| Job Requisition | No | Link | Related requisition |

### How to Create Job Opening
1. Click **Sidebar** → **Recruitment**
2. Click **Job Opening** in shortcuts
3. Click **+ Add Job Opening**
4. Enter **Job Title**
5. Select **Company**
6. Select **Designation**
7. Select **Department**
8. Select **Status** → "Open"
9. Select **Staffing Plan** (optional)
10. Enter **Vacancies**
11. Select **Posted On** date
12. Select **Closes On** date
13. Enter **Description** (full job description)
14. Select **Job Requisition** (if applicable)
15. Click **Save**

### How to Close Job Opening
1. Open the job opening
2. Change **Status** to "Closed"
3. Click **Save**

---

## Job Applicant

**URL:** `/app/job-applicant`

**Workspace:** Recruitment

Job Applicant tracks candidates who apply for positions.

### Job Applicant Fields

| Section | Field | Required | Description |
|---------|-------|----------|-------------|
| **Basic** | Applicant Name | Yes | Candidate name |
| | Email Address | Yes | Contact email |
| | Phone Number | No | Contact phone |
| | Job Title | Yes | Applied position |
| | Status | Yes | Application status |
| **Source** | Source | No | How they found us |
| | Source Name | No | Referral name |
| **Resume** | Resume Attachment | No | Upload CV |
| | Cover Letter | No | Cover letter text |
| **Rating** | Rating | No | Candidate rating |

### Job Applicant Status Options

| Status | Description |
|--------|-------------|
| Open | New application |
| Replied | Initial response sent |
| Accepted | Moving forward |
| Rejected | Not selected |
| Hold | On hold |

### How to Add Job Applicant (Manual)
1. Click **Sidebar** → **Recruitment**
2. Click **Job Applicant** in shortcuts
3. Click **+ Add Job Applicant**
4. Enter **Applicant Name**
5. Enter **Email Address**
6. Enter **Phone Number**
7. Select **Job Title** (job opening)
8. Select **Status** → "Open"
9. Select **Source** (Job Portal/Referral/etc.)
10. Click **Resume Attachment** → upload CV
11. Enter **Cover Letter** (optional)
12. Click **Save**

### How to Update Applicant Status
1. Open the job applicant record
2. Change **Status** (e.g., "Accepted")
3. Add notes in **Notes** section
4. Click **Save**

### How to Schedule Interview from Applicant
1. Open the job applicant record
2. Click **Create** → **Interview**
3. Interview form opens with applicant linked
4. Complete interview details (see Interview section)

---

## Interview

**URL:** `/app/interview`

**Workspace:** Recruitment

Interview schedules and tracks candidate interviews.

### Interview Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Job Applicant | Yes | Link | Candidate reference |
| Job Opening | Yes | Link | Position |
| Interview Round | Yes | Link | Round type |
| Scheduled On | Yes | Datetime | Interview date/time |
| Status | Yes | Select | Pending/Under Review/Cleared/Rejected |
| Interviewers | Yes | Table | Interview panel |
| Average Rating | Auto | Float | Average score |
| Expected Skill Set | No | Table | Skills to assess |
| Interview Feedback | No | Table | Feedback entries |

### Interviewers Table

| Field | Required | Description |
|-------|----------|-------------|
| Interviewer | Yes | User conducting interview |
| Is Mandatory | No | Required attendance |

### How to Schedule Interview
1. Click **Sidebar** → **Recruitment**
2. Click **Interview** in shortcuts
3. Click **+ Add Interview**
4. Select **Job Applicant**
5. Select **Job Opening**
6. Select **Interview Round** (e.g., "Technical Round")
7. Select **Scheduled On** (date and time)
8. Select **Status** → "Pending"
9. In **Interviewers** table:
   - Click **Add Row**
   - Select **Interviewer** (user)
   - Check **Is Mandatory** if required
   - Add more interviewers as needed
10. In **Expected Skill Set** table (optional):
    - Add skills to evaluate
11. Click **Save**
12. Click **Submit** (sends calendar invites)

### How to Submit Interview Feedback (Interviewer)
1. Click **Sidebar** → **Recruitment**
2. Click **Interview** in shortcuts
3. Filter by **Interviewers** → your name
4. Open the interview
5. Scroll to **Interview Feedback** section
6. Click **Add Row**
7. Select your name as **Interviewer**
8. Enter **Feedback**
9. Enter **Rating** (1-5)
10. Select **Result** (Cleared/Rejected)
11. Click **Save**

### How to Update Interview Result
1. Open the interview
2. Review all feedback
3. Change **Status**:
   - "Cleared" if passed
   - "Rejected" if not selected
   - "Under Review" if pending decision
4. Click **Save**

---

## Interview Round

**URL:** `/app/interview-round`

**Workspace:** Recruitment

Interview Round defines types of interview stages.

### How to Create Interview Round
1. Press `Ctrl + K` → type "Interview Round"
2. Click **+ Add Interview Round**
3. Enter **Round Name** (e.g., "HR Screening")
4. Enter **Expected Average Rating** (optional)
5. Click **Save**

### Common Interview Rounds

| Round | Description |
|-------|-------------|
| HR Screening | Initial HR call |
| Technical Round | Technical assessment |
| Coding Test | Programming test |
| Manager Round | Hiring manager interview |
| Culture Fit | Team/culture assessment |
| Final Round | Executive interview |

---

## Job Offer

**URL:** `/app/job-offer`

**Workspace:** Recruitment

Job Offer extends a formal offer to selected candidates.

### Job Offer Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Job Applicant | Yes | Link | Candidate |
| Applicant Name | Auto | Data | From applicant |
| Applicant Email | Auto | Data | From applicant |
| Company | Yes | Link | Offering company |
| Designation | Yes | Link | Job title |
| Offer Date | Yes | Date | Date of offer |
| Status | Yes | Select | Awaiting Response/Accepted/Rejected |
| Offer Terms | No | Table | Compensation details |

### Offer Terms Table

| Field | Required | Description |
|-------|----------|-------------|
| Offer Term | Yes | Term type |
| Value | Yes | Term value |

### How to Create Job Offer
1. Click **Sidebar** → **Recruitment**
2. Click **Job Offer** in shortcuts
3. Click **+ Add Job Offer**
4. Select **Job Applicant**
5. Select **Company**
6. Select **Designation**
7. Select **Offer Date**
8. Select **Status** → "Awaiting Response"
9. In **Offer Terms** table:
   - Click **Add Row**
   - Select **Offer Term** (e.g., "Base Salary")
   - Enter **Value** (e.g., "$5,000/month")
   - Add more terms (bonus, benefits, etc.)
10. Click **Save**
11. Click **Submit**

### How to Send Job Offer
1. Open the job offer
2. Click **Menu** (⋮) → **Email**
3. Select email template
4. Review and customize email
5. Click **Send**

### How to Update Offer Status
1. Open the job offer
2. Change **Status**:
   - "Accepted" if candidate accepts
   - "Rejected" if candidate declines
3. Click **Save**

### How to Create Employee from Job Offer
1. Open accepted job offer
2. Click **Create** → **Employee**
3. Employee form opens with details pre-filled
4. Complete remaining fields
5. Click **Save**

---

## Appointment Letter

**URL:** `/app/appointment-letter`

**Workspace:** Recruitment

Appointment Letter generates formal employment letters for new hires.

### Appointment Letter Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Job Applicant | Yes | Link | Candidate |
| Company | Yes | Link | Company |
| Appointment Letter Template | Yes | Link | Letter template |
| Job Offer | No | Link | Related offer |
| Appointment Date | Yes | Date | Start date |

### How to Create Appointment Letter
1. Click **Sidebar** → **Recruitment**
2. Click **Appointment Letter** in shortcuts
3. Click **+ Add Appointment Letter**
4. Select **Job Applicant**
5. Select **Company**
6. Select **Appointment Letter Template**
7. Select **Job Offer** (if applicable)
8. Select **Appointment Date**
9. Click **Save**
10. Click **Print** to generate letter

---

## Employee Referral

**URL:** `/app/employee-referral`

**Workspace:** Recruitment

Employee Referral tracks candidates referred by existing employees.

### Employee Referral Fields

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| Referrer | Yes | Link | Referring employee |
| Referral Name | Yes | Data | Candidate name |
| Referral Email | Yes | Data | Candidate email |
| For Job Opening | Yes | Link | Position |
| Status | Yes | Select | Pending/Accepted/Rejected |
| Resume | No | Attach | Candidate CV |

### How to Submit Employee Referral (Employee)
1. Click **Sidebar** → **Recruitment**
2. Click **Employee Referral** in shortcuts
3. Click **+ Add Employee Referral**
4. **Referrer** auto-fills with your name
5. Enter **Referral Name**
6. Enter **Referral Email**
7. Select **For Job Opening**
8. Click **Resume** → upload CV
9. Click **Save**
10. Click **Submit**

### How to Process Referral (HR)
1. Click **Sidebar** → **Recruitment**
2. Click **Employee Referral**
3. Filter by **Status** → "Pending"
4. Open the referral
5. Review candidate details
6. Click **Create Job Applicant** to add to pipeline
7. Update **Status** accordingly

---

## Recruitment Analytics Report

**URL:** `/app/query-report/Recruitment Analytics`

**Workspace:** Recruitment

### How to View Recruitment Analytics
1. Click **Sidebar** → **Recruitment**
2. Click **Recruitment Analytics** in Reports
3. Select **Company**
4. Select date range
5. View metrics:
   - Applications by source
   - Conversion rates
   - Time to hire
   - Offers accepted/rejected

---

## Quick Reference

### Recruitment Workflow
```
Staffing Plan → Job Requisition → Job Opening → Job Applicant → Interview → Job Offer → Appointment Letter → Employee
```

### Key URLs

| Document | URL |
|----------|-----|
| Staffing Plan | `/app/staffing-plan` |
| Job Requisition | `/app/job-requisition` |
| Job Opening | `/app/job-opening` |
| Job Applicant | `/app/job-applicant` |
| Interview | `/app/interview` |
| Interview Round | `/app/interview-round` |
| Job Offer | `/app/job-offer` |
| Appointment Letter | `/app/appointment-letter` |
| Employee Referral | `/app/employee-referral` |

### Recruitment Setup Checklist
- [ ] Create Interview Rounds
- [ ] Create Appointment Letter Templates
- [ ] Create Staffing Plan
- [ ] Create Job Openings
- [ ] Configure interview reminders (HR Settings)

### Required Roles
| Action | Required Role |
|--------|---------------|
| Create staffing plan | HR Manager |
| Create job opening | HR User, HR Manager |
| Add applicants | HR User, HR Manager |
| Conduct interviews | Interviewer |
| Submit feedback | Interviewer |
| Create job offer | HR Manager |
| Submit referral | Employee |

---

## 11. Career Portal (Public Jobs Website)

**Public URL:** `https://d11okjnno7fxem.cloudfront.net/jobs`

### Overview
HRDL8 has a built-in public career portal at `/jobs`. External candidates can browse open positions, search, filter, and apply — **no login required**. Job Openings with "Publish on website" enabled automatically appear here.

### What the Career Portal Shows
- Job cards with: Job Title, Company, Posted Date, Employment Type badge (Full-time/Part-time), Location, Department, Salary Range (if published), Applications Received count (if published), Closing Date
- Left sidebar filters: Company, Department, Employment Type, Location
- Search bar to search by job title or description
- Sort by posting date (ascending/descending)
- Pagination (20 jobs per page)
- Mobile-responsive with slide-up filter drawer

### Steps to Publish a Job on the Career Portal

1. Go to **Sidebar → Recruitment → Jobs → Job Opening** (`/app/job-opening`)
2. Open an existing Job Opening or click **+ Add Job Opening**
3. Fill in the required fields: **Job Title**, **Company**, **Designation**
4. Scroll to the website section
5. Check **Publish on website** — this makes the job visible at `/jobs`
6. Optionally fill in:
   - **Location** — shows on the job card with a map pin icon
   - **Employment Type** — shows as a colored badge (green for Full-time, orange for Part-time)
   - **Salary Range** (Lower Range / Upper Range / Currency / Salary Paid Per) — only visible if you also check **Publish Salary Range**
   - **Closes On** — shows closing date on the job card
   - **Publish Applications Received** — shows applicant count on the card
   - **Description** — full job description shown on the detail page (supports rich text)
7. Make sure **Status** is set to **Open**
8. Click **Save**
9. The job now appears at `https://d11okjnno7fxem.cloudfront.net/jobs`

### How the Individual Job Page Works

Each published job gets its own page at `/{route}` (auto-generated from job title).

The detail page shows:
- Job Title (large heading)
- Company name and posted date
- **Apply Now** button (top-right on desktop, sticky bottom on mobile)
- Detail cards with icons for: Location, Department, Salary Range, Employment Type, Applications Received, Closes On date
- Full job description

### How External Candidates Apply

1. Candidate visits `https://d11okjnno7fxem.cloudfront.net/jobs`
2. Browses or searches for a job
3. Clicks on a job card to view details
4. Clicks **Apply Now** button
5. Gets redirected to `/job_application/new?job_title={job-opening-id}`
6. Fills in the application form (name, email, cover letter, resume upload)
7. Submits the application
8. A **Job Applicant** record is automatically created in the system at `/app/job-applicant`
9. HR team can review it from **Sidebar → Recruitment → Job Applicant**

### Custom Application Route

You can redirect applicants to an external application form:
1. Open the Job Opening
2. Set **Job Application Route** to your custom URL (e.g., an external ATS link)
3. The **Apply Now** button will redirect to that URL instead

### Steps to Unpublish / Close a Job

1. Go to `/app/job-opening`
2. Open the Job Opening
3. Either:
   - Uncheck **Publish on website** (hides from portal but keeps status Open)
   - Change **Status** to **Closed** (shows "Opening closed" on the detail page)
4. Click **Save**

### Career Portal Filters

The portal auto-generates filters based on published jobs. Available filters:
- **Company** — filter by company name
- **Department** — filter by department
- **Employment Type** — filter by Full-time, Part-time, Contract, etc.
- **Location** — filter by branch/location

Filters appear as checkboxes on the left sidebar (desktop) or in a slide-up drawer (mobile).

### Quick Reference

| Action | URL |
|--------|-----|
| View career portal | `/jobs` |
| View individual job | `/{auto-generated-route}` |
| Apply for a job | Click **Apply Now** on job page |
| Manage job openings | `/app/job-opening` |
| Review applications | `/app/job-applicant` |
