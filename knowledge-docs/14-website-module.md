# HRDL8 Knowledge Base: Website Module

**Navigation:** Sidebar → Website
**URL:** `/app/website`

---

## Overview

The Website module is a built-in CMS (Content Management System) that lets you create and manage public-facing web pages, blogs, forms, and a knowledge base — all without leaving the HRDL8 desk. Public pages are accessible without login.

---

## 1. Website Settings

**URL:** `/app/website-settings`

### Steps to Configure

1. Click **Website** in the sidebar
2. Under **Setup**, click **Website Settings**
3. Configure the following sections:

#### Brand
4. Enter **App Name** — shown in browser tab title
5. Upload **Banner Image** or **Favicon**

#### Top Bar
6. Scroll to **Top Bar** section
7. Click **Add Row** to add navigation menu items
8. Enter **Label** (e.g., "Home", "Jobs", "About", "Contact")
9. Enter **URL** (e.g., `/`, `/jobs`, `/about`, `/contact`)
10. Check **Open in New Tab** if needed
11. Set **Parent Label** to create dropdown menus

#### Footer
12. Scroll to **Footer** section
13. Add footer links, copyright text, and social media links
14. Enter **Footer Address** and **Footer Logo**

#### Integrations
15. Enter **Google Analytics ID** for tracking
16. Add **Head HTML** for custom meta tags or scripts

17. Click **Save**

---

## 2. Website Theme

**URL:** `/app/website-theme`

### Steps to Create/Edit a Theme

1. Click **Website** in the sidebar
2. Under **Setup**, click **Website Theme**
3. Click **+ Add Website Theme** or edit existing
4. Configure:
   - **Theme Name**
   - **Font Family** and **Font Size**
   - **Primary Color**, **Text Color**, **Background Color**
   - **Button Style** (rounded, square)
   - **Custom CSS** — add any custom styles
5. Click **Save**
6. Go to **Website Settings** → set this as the active theme

---

## 3. Website Script

**URL:** `/app/website-script`

### Steps to Add Custom JavaScript

1. Click **Website** in the sidebar
2. Under **Setup**, click **Website Script**
3. Enter JavaScript code in the editor
4. This script runs on **all public website pages**
5. Click **Save**

---

## 4. Web Page (Static Pages)

**URL:** `/app/web-page`

### Steps to Create a Web Page

1. Click **Website** in the sidebar
2. Under **Web Site**, click **Web Page**
3. Click **+ Add Web Page**
4. Enter **Title** (required) — e.g., "About Our Company"
5. Enter **Route** — the URL path (e.g., `about-us` makes it accessible at `/about-us`)
6. Check **Published** to make it live
7. Add content using:
   - **Content Type**: Markdown, Rich Text, or Page Builder
   - For **Page Builder**: click **Add Row** to add blocks (Hero, Section, CTA, etc.)
8. Optionally set **Meta Title**, **Meta Description**, **Meta Image** for SEO
9. Click **Save**
10. Visit `https://d11okjnno7fxem.cloudfront.net/{route}` to see the page

---

## 5. Blog

### 5.1 Blog Category

**URL:** `/app/blog-category`

1. Click **Website** in the sidebar
2. Under **Blog**, click **Blog Category**
3. Click **+ Add Blog Category**
4. Enter **Category Name** (e.g., "Company News", "HR Tips")
5. Click **Save**

### 5.2 Blogger (Author Profile)

**URL:** `/app/blogger`

1. Click **Website** in the sidebar
2. Under **Blog**, click **Blogger**
3. Click **+ Add Blogger**
4. Enter **Full Name**, **Short Name**
5. Upload **Avatar**
6. Link to **User** account
7. Click **Save**

### 5.3 Blog Post

**URL:** `/app/blog-post`

1. Click **Website** in the sidebar
2. Under **Blog**, click **Blog Post**
3. Click **+ Add Blog Post**
4. Enter **Title** (required)
5. Select **Blog Category**
6. Select **Blogger** (author)
7. Write content in the **Content** editor (supports rich text and markdown)
8. Upload **Meta Image** (shown as thumbnail)
9. Check **Published** to make it live
10. Click **Save**
11. Blog is accessible at `https://d11okjnno7fxem.cloudfront.net/blog/{route}`
12. All blogs listed at `/blog`

---

## 6. About Us Page

**URL:** `/app/about-us-settings`
**Public URL:** `/about`

### Steps to Configure

1. Click **Website** in the sidebar
2. Under **Setup**, click **About Us Settings**
3. Enter **Company Introduction** (rich text)
4. Add **Company History** entries (year + highlight)
5. Add **Team Members**:
   - Click **Add Row**
   - Enter Name, Designation, Bio
   - Upload Photo
6. Click **Save**
7. Page is live at `/about`

---

## 7. Contact Us Page

**URL:** `/app/contact-us-settings`
**Public URL:** `/contact`

### Steps to Configure

1. Click **Website** in the sidebar
2. Under **Setup**, click **Contact Us Settings**
3. Enter **Heading** and **Introduction**
4. Enter **Address** (shown on the page)
5. Configure email settings for form submissions
6. Click **Save**
7. Contact form is live at `/contact` — submissions create **Communication** records

---

## 8. Web Form (Public Forms)

**URL:** `/app/web-form`

### Steps to Create a Web Form

1. Click **Website** in the sidebar
2. Under **Web Site**, click **Web Form**
3. Click **+ Add Web Form**
4. Enter **Title** (required)
5. Enter **Route** (URL path)
6. Select **Doc Type** — the form maps to this DocType (e.g., Job Applicant, Feedback)
7. Check **Published** to make it live
8. Check **Allow Guest** if no login should be required
9. Add fields:
   - Click **Add Row** in the **Web Form Fields** table
   - Select **Fieldname** (from the linked DocType)
   - Set **Label**, **Required**, **Hidden** as needed
10. Optionally add **Introduction** text and **Success URL** (redirect after submit)
11. Click **Save**
12. Form is accessible at `/{route}`

### Use Cases
- External job application form
- Employee feedback/survey form
- Exit interview questionnaire (linked to HR Settings → Exit Questionnaire Web Form)

---

## 9. Portal Settings

**URL:** `/app/portal-settings`

### Overview
The portal is a self-service area for logged-in users. Employees can view their own records (leave, salary slips, etc.) without accessing the full desk.

### Steps to Configure

1. Click **Website** in the sidebar
2. Under **Portal**, click **Portal Settings**
3. Configure **Portal Menu Items**:
   - Each item maps to a DocType list filtered to the logged-in user
   - Default items: Leave Application, Salary Slip, Expense Claim, etc.
4. Set **Default Portal Role** (usually "Employee")
5. Set **Custom Homepage** for portal users
6. Click **Save**

### How Employees Access the Portal
1. Employee logs in at `https://d11okjnno7fxem.cloudfront.net/login`
2. They see the portal homepage (not the full desk)
3. Sidebar shows portal menu items (Leave, Salary Slip, etc.)
4. They can only see their own records

---

## 10. Knowledge Base (Help Articles)

**URL:** `/app/help-article`
**Public URL:** `/kb`

### 10.1 Help Category

**URL:** `/app/help-category`

1. Click **Website** in the sidebar
2. Under **Knowledge Base**, click **Help Category**
3. Click **+ Add Help Category**
4. Enter **Category Name** (e.g., "Getting Started", "Leave & Attendance", "Payroll")
5. Click **Save**

### 10.2 Help Article

**URL:** `/app/help-article`

1. Click **Website** in the sidebar
2. Under **Knowledge Base**, click **Help Article**
3. Click **+ Add Help Article**
4. Enter **Title** (required)
5. Select **Category**
6. Select **Level**: Beginner, Intermediate, Expert
7. Write content in the editor (supports rich text, images, code blocks)
8. Check **Published**
9. Click **Save**
10. Article is accessible at `/kb/{category}/{article-route}`
11. All articles browsable at `/kb`

---

## 11. Website Sidebar

**URL:** `/app/website-sidebar`

### Steps to Create a Sidebar

1. Click **Website** in the sidebar
2. Under **Web Site**, click **Website Sidebar**
3. Click **+ Add Website Sidebar**
4. Enter **Title**
5. Add sidebar items:
   - Click **Add Row**
   - Enter **Title** and **Route** for each link
6. Click **Save**
7. Assign this sidebar to specific Web Pages

---

## 12. Website Slideshow

**URL:** `/app/website-slideshow`

### Steps to Create a Slideshow

1. Click **Website** in the sidebar
2. Under **Web Site**, click **Website Slideshow**
3. Click **+ Add Website Slideshow**
4. Enter **Slideshow Name**
5. Add slides:
   - Click **Add Row**
   - Upload **Image**
   - Enter **Heading** and **Description**
6. Click **Save**
7. Use this slideshow in Web Pages or other content

---

## 13. Website Route Meta (SEO)

**URL:** `/app/website-route-meta`

### Steps to Add SEO Meta Tags

1. Click **Website** in the sidebar
2. Under **Web Site**, click **Website Route Meta**
3. Click **+ Add Website Route Meta**
4. Enter **Route** (e.g., `jobs`, `about`)
5. Add meta tags:
   - Click **Add Row**
   - Enter **Key** (e.g., `description`, `og:image`)
   - Enter **Value**
6. Click **Save**

---

## Quick Reference

| Feature | Desk URL | Public URL |
|---------|----------|------------|
| Website Settings | `/app/website-settings` | N/A (configuration) |
| Website Theme | `/app/website-theme` | N/A (styling) |
| Web Page | `/app/web-page` | `/{custom-route}` |
| Blog Post | `/app/blog-post` | `/blog/{route}` |
| About Us | `/app/about-us-settings` | `/about` |
| Contact Us | `/app/contact-us-settings` | `/contact` |
| Web Form | `/app/web-form` | `/{custom-route}` |
| Portal Settings | `/app/portal-settings` | `/me` (logged-in users) |
| Help Article | `/app/help-article` | `/kb/{category}/{route}` |
| Career Portal | `/app/job-opening` | `/jobs` |

---

*Last updated: April 2026*
