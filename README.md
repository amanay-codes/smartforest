# 🌲 Smart Forest — Incident Management System

> **CSC 3324 — Software Engineering, Spring 2026**
> Al Akhawayn University in Ifrane, Morocco
> Team: Software Rangers | Supervisor: Dr. Chakiri Houda

---

> [!IMPORTANT]
> **⚠️ The `.env` file is REQUIRED. The app will NOT run without it.**
> This file is not included in the repository for security reasons.
> Follow the [Environment Variables](#7-environment-variables-env-file) section carefully before running the project.

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Live Demo](#2-live-demo)
3. [Features](#3-features)
4. [Tech Stack](#4-tech-stack)
5. [Prerequisites](#5-prerequisites)
6. [Local Setup — Step by Step](#6-local-setup--step-by-step)
7. [Environment Variables (.env file)](#7-environment-variables-env-file)
8. [Creating an Admin Account](#8-creating-an-admin-account)
9. [Project Structure](#9-project-structure)
10. [URL Reference](#10-url-reference)
11. [Database Schema](#11-database-schema)
12. [Deployment](#12-deployment)
13. [Team](#13-team)

---

## 1. Project Overview

**Smart Forest** is a web-based incident management system designed to help citizens and forest administrators report, track, and resolve forest-related incidents in Morocco.

### The Problem It Solves

Forest incidents — wildfires, illegal logging, pollution, and general forest damage — are often underreported because there is no easy, centralized way for citizens to file a report and for authorities to act on it. Smart Forest bridges that gap.

### Who Uses It

| Role | What They Can Do |
|------|-----------------|
| **Citizen (regular user)** | Register, log in, submit incident reports with photos, track the status of their own reports |
| **Admin (forest authority)** | View all reports from all users, filter by type or status, update report status, add admin notes, view statistics, manage users |

---

## 2. Live Demo

The project is deployed and accessible at:

**[https://smartforest.onrender.com](https://smartforest.onrender.com)**

> **Note:** The app is hosted on Render's free tier. If it hasn't been visited recently, it may take **30–50 seconds to wake up** on your first visit. This is normal — just wait and the page will load.

---

## 3. Features

### For Citizen Users
- **Register & Log In** — Create an account and securely log in
- **Submit Incident Reports** — Report a forest incident with a description, location, type, and optional photo
- **Track Report Status** — See whether your report is Pending, In Progress, or Resolved
- **Personal Dashboard** — View a summary of your reports with statistics and a monthly activity chart
- **Report History** — Browse all your past reports in one place

### For Admin Users
- **Admin Dashboard** — View all reports submitted by all users in a centralized view
- **Filter & Search** — Filter reports by incident type, status, or search by keyword (description, location, or username)
- **Update Report Status** — Change a report's status and add internal admin notes
- **Statistics Page** — See breakdown of reports by type and by status with counts
- **Users Management Page** — View all registered users and how many reports each has submitted

---

## 4. Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend Framework** | Django 6.0.4 |
| **Programming Language** | Python 3.10+ |
| **Database** | PostgreSQL (hosted on [Neon](https://neon.tech) — cloud) |
| **Image Storage** | [Cloudinary](https://cloudinary.com) |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript (no Bootstrap) |
| **Static Files** | WhiteNoise |
| **Production Server** | Gunicorn |
| **Deployment Platform** | [Render](https://render.com) (free tier) |

---

## 5. Prerequisites

Before you start, make sure the following are installed on your laptop:

### 1. Python 3.10 or higher
Check if you have it:
```bash
python --version
```
Download from [https://www.python.org/downloads/](https://www.python.org/downloads/) if needed.

### 2. pip (Python package manager)
Usually comes with Python. Check with:
```bash
pip --version
```

### 3. Git
Check with:
```bash
git --version
```
Download from [https://git-scm.com/downloads](https://git-scm.com/downloads) if needed.

### 4. A Code Editor
We recommend **Visual Studio Code** — [https://code.visualstudio.com/](https://code.visualstudio.com/)

> **No PostgreSQL installation needed!** The database is hosted in the cloud (Neon). You just need the credentials in your `.env` file.

---

## 6. Local Setup — Step by Step

Follow these steps **in order**. Do not skip any step.

### Step 1 — Clone the Repository

Open your terminal (Command Prompt, PowerShell, or Terminal) and run:

```bash
git clone https://github.com/amanay-codes/smartforest.git
```

### Step 2 — Navigate Into the Project Folder

```bash
cd smartforest
```

You should now be inside the `smartforest/` folder. All remaining commands must be run from here.

### Step 3 — (Recommended) Create a Virtual Environment

A virtual environment keeps the project's dependencies isolated from your system Python. This is optional but strongly recommended.

```bash
python -m venv .venv
```

Then activate it:

- **Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
- **Windows (Command Prompt):**
  ```cmd
  .venv\Scripts\activate.bat
  ```
- **Mac / Linux:**
  ```bash
  source .venv/bin/activate
  ```

You'll know it's active when you see `(.venv)` at the beginning of your terminal prompt.

### Step 4 — Install Dependencies

```bash
python -m pip install -r requirements.txt
```

This installs Django and all other required packages. It may take a minute.

### Step 5 — Create the `.env` File

**This is the most important step.** The app cannot run without this file.

Create a file named exactly `.env` in the root of the project folder (the same folder that contains `manage.py`).

See the full instructions in [Section 7 — Environment Variables](#7-environment-variables-env-file) below.

### Step 6 — Run Database Migrations

This sets up the database tables:

```bash
python manage.py migrate
```

You should see output like `Applying incidents.0001_initial... OK`. That means it worked.

### Step 7 — Start the Development Server

```bash
python manage.py runserver
```

### Step 8 — Open the App in Your Browser

Go to: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

The login page should appear. You can register a new user account, or create an admin account (see [Section 8](#8-creating-an-admin-account)).

---

## 7. Environment Variables (.env file)

---

> ### ⚠️ CRITICAL — READ THIS CAREFULLY
>
> The `.env` file stores secret configuration values (database passwords, API keys, etc.).
> It is **intentionally excluded** from the Git repository so these secrets are never made public.
>
> **You must create this file yourself before the app will run.**
>
> - The file must be named exactly **`.env`** (with a dot at the start, no other extension)
> - It must be placed in the **root of the project folder** — the same folder that contains `manage.py`
> - Contact the team for the actual credential values (database password, Cloudinary keys)

---

### How to Create the `.env` File

Create a new file called `.env` in the project root and paste the following content into it, replacing the placeholder values as instructed:

```env
# ============================================================
# Django Core Settings
# ============================================================

# A secret key used by Django for security. This value is fine for local use.
DJANGO_SECRET_KEY=django-insecure-local-smartforest-change-me

# Set to True for local development (shows detailed error pages)
DJANGO_DEBUG=True

# Hosts that are allowed to access the app
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1


# ============================================================
# Database — Neon PostgreSQL (Cloud)
# ============================================================
# No local PostgreSQL installation needed.
# The database is hosted on Neon and shared with the live site.
# Contact the team for the actual DB_PASSWORD and DATABASE_URL values.

DB_ENGINE=postgresql
DB_NAME=neondb
DB_USER=neondb_owner
DB_PASSWORD=CONTACT_TEAM_FOR_PASSWORD
DB_HOST=ep-morning-darkness-al4cl046-pooler.c-3.eu-central-1.aws.neon.tech
DB_PORT=5432
DB_SSLMODE=require

# Alternatively, you can use a single connection URL (ask team for the full value):
# DATABASE_URL=CONTACT_TEAM_FOR_FULL_URL


# ============================================================
# Cloudinary — Image Storage
# ============================================================
# Required for image uploads to work.
# Contact the team for the actual values below.

USE_CLOUDINARY=True
CLOUDINARY_CLOUD_NAME=CONTACT_TEAM_FOR_VALUE
CLOUDINARY_API_KEY=CONTACT_TEAM_FOR_VALUE
CLOUDINARY_API_SECRET=CONTACT_TEAM_FOR_VALUE
```

> **Contact the team** to receive the actual values for `DB_PASSWORD`, `DATABASE_URL`, `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, and `CLOUDINARY_API_SECRET`.
>
> The database is cloud-hosted on Neon — **no local PostgreSQL installation is needed**. Once you have the correct credentials in your `.env` file, the app connects directly to the shared cloud database.

---

## 8. Creating an Admin Account

After running `python manage.py migrate`, you can create a superuser (admin) account with:

```bash
python manage.py createsuperuser
```

You will be prompted to enter:
- A username
- An email address (optional)
- A password (typed twice)

Once created, start the server and go to **[http://127.0.0.1:8000](http://127.0.0.1:8000)**. Log in with those credentials. Because the account is a superuser (staff), you will be redirected automatically to the **Admin Dashboard** at `/admin-dashboard/`.

---

## 9. Project Structure

```
smartforest/                        ← Root project folder
│
├── manage.py                       ← Django's command-line tool (run all commands from here)
├── requirements.txt                ← Python package dependencies
├── build.sh                        ← Build script used by Render for deployment
├── .env                            ← ⚠️ Your secret config file (you must create this)
├── .env.example                    ← Template showing what the .env file should look like
├── .gitignore                      ← Files excluded from Git (includes .env)
│
├── smartforest/                    ← Django project configuration package
│   ├── settings.py                 ← All app settings (reads from .env)
│   ├── urls.py                     ← Root URL routing
│   ├── wsgi.py                     ← WSGI entry point (used by Gunicorn in production)
│   └── asgi.py                     ← ASGI entry point (for async support)
│
└── incidents/                      ← Main Django app (all app logic lives here)
    ├── models.py                   ← Database table definitions (IncidentReport)
    ├── views.py                    ← Page logic — what happens when a URL is visited
    ├── urls.py                     ← App-level URL patterns
    ├── forms.py                    ← Registration form, incident report form, status form
    ├── admin.py                    ← Django admin panel configuration
    ├── apps.py                     ← App configuration
    ├── tests.py                    ← Automated tests
    │
    ├── migrations/                 ← Database migration files (auto-generated)
    │   ├── 0001_initial.py
    │   └── 0002_alter_incidentreport_options.py
    │
    └── templates/incidents/        ← HTML templates for every page
        ├── base.html               ← Shared layout (header, nav, footer)
        ├── login.html              ← Login page
        ├── register.html           ← Registration page
        ├── about.html              ← About page
        ├── dashboard.html          ← Citizen user dashboard
        ├── my_reports.html         ← User's report history
        ├── submit_report.html      ← New incident report form
        ├── report_detail.html      ← Single report view (citizen)
        ├── admin_dashboard.html    ← Admin: all reports with filters
        ├── admin_report_detail.html← Admin: edit report status & notes
        ├── admin_statistics.html   ← Admin: statistics breakdown
        └── admin_users.html        ← Admin: user list
```

---

## 10. URL Reference

| URL | Who Can Access | What It Does |
|-----|---------------|-------------|
| `/` | Everyone | Login page |
| `/register/` | Everyone | User registration page |
| `/about/` | Everyone | About the project |
| `/logout/` | Logged-in users | Logs the user out and redirects to login |
| `/dashboard/` | Logged-in citizens | Personal dashboard with report stats and chart |
| `/my-reports/` | Logged-in citizens | List of the user's own submitted reports |
| `/report/submit/` | Logged-in citizens | Form to submit a new incident report |
| `/report/<id>/` | Logged-in citizens | Detail view of a single report (own reports only) |
| `/admin-dashboard/` | Admin (staff) only | All reports from all users, with filter & search |
| `/admin-dashboard/report/<id>/` | Admin (staff) only | Edit a report's status and add admin notes |
| `/admin-dashboard/statistics/` | Admin (staff) only | Reports breakdown by type and status |
| `/admin-dashboard/users/` | Admin (staff) only | All registered users and their report counts |
| `/admin/` | Superuser only | Django's built-in admin panel |

---

## 11. Database Schema

The app uses two main database tables provided by Django:

### `auth_user` (built-in Django table)
Stores all registered user accounts. Key fields: `id`, `username`, `email`, `password` (hashed), `is_staff` (True for admins).

### `incidents_incidentreport` (custom table)

| Field | Type | Description |
|-------|------|-------------|
| `id` | Integer (auto) | Unique report ID, assigned automatically |
| `user` | Foreign Key → User | The citizen who submitted the report |
| `incident_type` | Text (choices) | One of: `wildfire`, `illegal_logging`, `pollution`, `forest_damage` |
| `description` | Long Text | Detailed description of the incident |
| `location` | Text (max 255) | Where the incident occurred |
| `image` | Image file | Optional photo of the incident |
| `status` | Text (choices) | One of: `pending`, `in_progress`, `resolved` (default: `pending`) |
| `submitted_at` | Date & Time | Timestamp set automatically when the report is created |
| `admin_notes` | Long Text | Optional internal notes added by an admin |

**Note:** A report is flagged as "critical" if its type is `wildfire` or `forest_damage` **and** its status is `pending` or `in_progress`.

---

## 12. Deployment

The app is deployed on **Render** (free tier) and is live at:

**[https://smartforest.onrender.com](https://smartforest.onrender.com)**

The deployed version connects to the **same Neon PostgreSQL cloud database** as the local setup. This means:
- Reports submitted locally will appear on the live site, and vice versa (as long as you use the same credentials)
- User accounts are shared between local and deployed versions
- Images are stored on Cloudinary (also shared)

The `build.sh` script handles installing dependencies and running migrations automatically on each deploy.

---

## 13. Team

| Name | Role |
|------|------|
| **Rania Bettioui** | Team Lead |
| **Reda Benhaimoud** | Developer |
| **Ilyass Lhafi** | Developer |
| **Fatima Ezzahra Fakir** | Business Analyst |
| **Dr. Chakiri Houda** | Supervisor |

**GitHub Repository:** [https://github.com/amanay-codes/smartforest](https://github.com/amanay-codes/smartforest)

---

*CSC 3324 — Software Engineering, Spring 2026 — Al Akhawayn University in Ifrane*
