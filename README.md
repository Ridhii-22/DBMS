# 📊 Smart Dues Tracker for Shopkeepers

A Django-based web application to help shopkeepers efficiently track and manage customer dues. Built with **Django 4.x**, **Python**, **MySQL**, and **XAMPP**, this project provides a user-friendly interface for managing customer information, tracking outstanding dues, and marking payments.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation Guide](#installation-guide)
- [Database Setup](#database-setup)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
- [Usage Guide](#usage-guide)
- [Troubleshooting](#troubleshooting)
- [Common Commands Reference](#common-commands-reference)
- [Future Enhancements](#future-enhancements)
- [Quick Start Checklist](#quick-start-checklist)

---

## Project Overview

The **Smart Dues Tracker** is a web-based application designed for Indian shopkeepers to manage customer credits and dues:

- Register and maintain secure login credentials
- Add and manage customer information
- Track outstanding dues with descriptions and due dates
- Mark dues as paid
- View comprehensive dashboards with due summaries
- Search and filter customers

This project uses **Django 4.x** as the backend framework, **MySQL** via **XAMPP** for database management, and a responsive frontend with modern CSS styling.

---

## Features

#### 1. User Authentication
- Shopkeeper registration and login
- Secure password hashing with Django's built-in system
- Session management and logout functionality
- Role-based access control (login required for protected pages)

#### 2. Dashboard
- Overview of total customers
- Quick view of total pending dues amount
- Recent transactions display
- Visual statistics with stat cards

#### 3. Customer Management
- Add new customers with contact details
- Search customers by name or phone number
- View complete customer profiles with information
- List all customers with pending dues summary

#### 4. Dues Tracking
- Add dues for customers with amount and description
- Set due dates for tracking
- Mark dues as PAID or PENDING
- View complete dues history per customer
- Real-time calculation of total pending dues

#### 5. Admin Panel
- Django admin interface for data management
- View and filter shopkeepers, customers, and dues
- Direct database manipulation capability

### 🎨 User Interface

- Modern gradient-based design (purple/blue theme)
- Responsive layout that works on desktop and tablets
- Card-based dashboard with statistics
- Search functionality with live filtering
- Intuitive navigation with clear calls-to-action

---

## Technology Stack

### Backend
- **Framework**: Django 4.2.x
- **Language**: Python 3.8+
- **Database**: MySQL (via XAMPP)
- **Authentication**: Django's built-in User model
- **ORM**: Django ORM with querysets

### Frontend
- **HTML5**: Template structure
- **CSS3**: Responsive styling with gradients and flexbox/grid
- **JavaScript**: Minimal vanilla JS (ready for enhancements)
- **Template Engine**: Django Template Language (DTL)

### Database
- **MySQL Server**: XAMPP MySQL
- **Database Name**: dues_tracker_db
- **Port**: 3306 (default)

---

## Project Structure

```
dues_tracker/
│
├── dues_tracker/                    # Main project folder
│   ├── __init__.py
│   ├── settings.py                  # Django settings and configurations
│   ├── urls.py                      # Main URL routing
│   ├── asgi.py
│   └── wsgi.py
│
├── tracker/                         # Main app folder
│   ├── migrations/                  # Database migrations
│   ├── __init__.py
│   ├── admin.py                     # Admin panel configuration
│   ├── apps.py
│   ├── models.py                    # Database models (Shopkeeper, Customer, Due)
│   ├── views.py                     # View logic and request handlers
│   ├── urls.py                      # App-specific URL routing
│   └── tests.py
│
├── templates/                       # HTML template files
│   ├── base.html                    # Base template with navbar and styling
│   ├── login.html                   # Login page
│   ├── register.html                # Registration page
│   ├── dashboard.html               # Main dashboard
│   ├── customers.html               # Customers list page
│   ├── add_customer.html            # Add customer form
│   ├── customer_detail.html         # Customer detail view
│   ├── add_due.html                 # Add due form
│   └── due_detail.html              # Due detail view (optional)
│
├── static/                          # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
│
├── manage.py                        # Django management script
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

---

## Prerequisites

Before you begin, ensure you have the following installed on your system:

### Required Software

1. **Python 3.8 or higher**
   - Download from: https://www.python.org/downloads/
   - Verify: `python --version`

2. **XAMPP** (for MySQL and Apache)
   - Download from: https://www.apachefriends.org/
   - Includes MySQL Server, phpMyAdmin, and Apache

3. **Text Editor/IDE** (Visual Studio Code, PyCharm, etc.)
   - Recommended: Visual Studio Code with Python extension

### System Requirements

- Windows 10+, macOS, or Linux
- 2GB RAM minimum
- 500MB disk space
- Internet connection for initial setup

---

## Installation Guide

### Step 1: Install Python and XAMPP

**Download and Install Python**
1. Go to https://www.python.org/downloads/
2. Download Python 3.8 or later
3. During installation, **check "Add Python to PATH"**
4. Click "Install Now"

**Download and Install XAMPP**
1. Go to https://www.apachefriends.org/
2. Download XAMPP for your operating system
3. Run the installer and follow the setup wizard
4. When asked about components, ensure **MySQL** is selected

### Step 2: Create Project Directory

```bash
# Create a folder for your project
mkdir dues_tracker_project
cd dues_tracker_project

# Create a virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Django and Dependencies

```bash
# Install Django 4.2 and MySQL client
pip install Django==4.2
pip install mysqlclient

# Or install from requirements.txt:
pip install -r requirements.txt
```

**requirements.txt:**
```
Django==4.2
mysqlclient==2.2.0
```

### Step 4: Create Django Project

```bash
# Create the project
django-admin startproject dues_tracker .

# Create the tracker app
python manage.py startapp tracker

# Create templates folder
mkdir templates
```

### Step 5: Create Folder Structure

```bash
# Create additional folders
mkdir static
mkdir static/css
mkdir static/js
mkdir static/images
```

---

## Database Setup

### Step 1: Start XAMPP Services

1. **Open XAMPP Control Panel**
2. Click **"Start"** next to **MySQL**
3. Wait until it shows "Running" (green indicator)
4. (Optional) Click **"Start"** next to **Apache** if you want to use phpMyAdmin

### Step 2: Create Database in phpMyAdmin

1. **Open phpMyAdmin**
   - If Apache is running: http://localhost/phpmyadmin
   - Or use MySQL command line

2. **Create Database**
   ```sql
   CREATE DATABASE dues_tracker_db;
   ```

3. **Verify Database Created**
   - You should see `dues_tracker_db` in the left panel

### Step 3: Configure Django Settings

In `dues_tracker/settings.py`, configure the MySQL database connection:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dues_tracker_db',
        'USER': 'root',
        'PASSWORD': '',              # XAMPP default is empty
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Also ensure these settings are in place:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tracker',  # Our app
]

TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        # ...
    }
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/login/'
```

### Step 4: Run Migrations

```bash
# Create migration files based on models
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate
```

**Expected Output:**
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, tracker
Running migrations:
  Applying contenttypes.0001_initial...
  Applying auth.0001_initial...
  ... (more migrations)
  Applying tracker.0001_initial... OK
```

### Step 5: Create Superuser (Optional but Recommended)

```bash
python manage.py createsuperuser
```

Follow the prompts:
- Username: `admin`
- Email: `admin@example.com`
- Password: (choose a password)

---

## Running the Project

### Step 1: Ensure MySQL is Running

1. Open XAMPP Control Panel
2. Verify MySQL is showing "Running" (green indicator)

### Step 2: Start Django Development Server

```bash
# In your project directory with virtual environment activated
python manage.py runserver
```

**Expected Output:**
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 18, 2025 - 00:00:00
Django version 4.2, using settings 'dues_tracker.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Step 3: Access the Application

Open your web browser and navigate to:

- **Home Page**: http://127.0.0.1:8000/
- **Login Page**: http://127.0.0.1:8000/login/
- **Register Page**: http://127.0.0.1:8000/register/
- **Admin Panel**: http://127.0.0.1:8000/admin/ (login with superuser credentials)

---

## Usage Guide

### For First-Time Users

#### 1. Registration

1. Navigate to http://127.0.0.1:8000/register/
2. Fill in the registration form:
   - **Username**: Your unique username
   - **Email**: Your email address
   - **Password**: Strong password
   - **Shop Name**: Your shop's name
   - **Phone Number**: Your contact number
   - **Address**: Your shop's address
3. Click **"Register"**
4. You'll be redirected to login page

#### 2. Login

1. Navigate to http://127.0.0.1:8000/login/
2. Enter your **Username** and **Password**
3. Click **"Login"**
4. You'll be redirected to your **Dashboard**

#### 3. Add Customers

1. Click **"Customers"** in the navbar
2. Click **"+ Add Customer"** button
3. Fill in customer details:
   - **Customer Name**: Full name of customer
   - **Phone Number**: Contact number
   - **Address**: Customer's address (optional)
4. Click **"Add Customer"**

#### 4. Add Dues

1. Go to **Customers** page
2. Click on a customer card **"View Details"**
3. Click **"Add Due"** button
4. Fill in due details:
   - **Amount**: Due amount in rupees
   - **Description**: Reason for the due (e.g., "Grocery items")
   - **Due Date**: Expected payment date
5. Click **"Add Due"**

#### 5. Mark Dues as Paid

1. Go to customer details
2. Find the due in the list
3. Click **"Mark as Paid"** button
4. Due status will change to **"PAID"** (green)

#### 6. View Dashboard

1. Click **"Dashboard"** in the navbar
2. View statistics:
   - Total number of customers
   - Total pending dues amount
   - Recent transactions
3. Monitor your business at a glance

---

## Troubleshooting

### Issue 1: MySQL Connection Error

**Error Message:**
```
django.db.utils.OperationalError: (2002, "Can't connect to local MySQL server through socket '/tmp/mysql.sock'")
```

**Solution:**

1. **Verify XAMPP MySQL is running**
   - Open XAMPP Control Panel
   - Click "Start" next to MySQL
   - Wait for green indicator

2. **Check Database Credentials**
   ```python
   # In settings.py
   'USER': 'root',
   'PASSWORD': '',  # Ensure it's empty for XAMPP default
   'HOST': 'localhost',
   'PORT': '3306',
   ```

3. **Try Different Host**
   ```python
   'HOST': '127.0.0.1',  # Instead of 'localhost'
   ```

### Issue 2: Template Not Found Error

**Error Message:**
```
TemplateDoesNotExist at /login/
login.html
```

**Solution:**

1. **Verify Templates Folder Exists**
   ```bash
   # Ensure this directory exists:
   dues_tracker/templates/
   ```

2. **Check settings.py Configuration**
   ```python
   TEMPLATES = [
       {
           'DIRS': [os.path.join(BASE_DIR, 'templates')],
           # ...
       }
   ]
   ```

3. **Verify Template Files**
   - Ensure `login.html`, `dashboard.html`, etc. are in the `templates/` folder
   - Check file names for typos

### Issue 3: Static Files Not Loading (CSS/Images)

**Symptom:** Page loads but no styling

**Solution:**

1. **Collect Static Files**
   ```bash
   python manage.py collectstatic --noinput
   ```

2. **Verify Static Folder**
   ```bash
   # Ensure directory exists:
   dues_tracker/static/
   ```

3. **Check settings.py**
   ```python
   STATIC_URL = '/static/'
   STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
   ```

### Issue 4: Module Import Error

**Error Message:**
```
ModuleNotFoundError: No module named 'MySQLdb'
```

**Solution:**

```bash
# Install mysqlclient
pip install mysqlclient

# If that fails on Windows, try:
pip install mysqlclient==2.2.0
```

### Issue 5: Port 8000 Already in Use

**Error Message:**
```
OSError: [Errno 98] Address already in use
```

**Solution:**

```bash
# Use a different port
python manage.py runserver 8001

# Then access: http://127.0.0.1:8001/
```

### Issue 6: Blank Page After Login

**Symptom:** Page loads but shows only background gradient

**Solution:**

1. **Check Browser Console**
   - Press F12 to open Developer Tools
   - Check Console tab for JavaScript errors

2. **Verify Login Redirect**
   - Check if `LOGIN_REDIRECT_URL` is set in settings.py
   ```python
   LOGIN_REDIRECT_URL = '/dashboard/'
   ```

3. **Check Dashboard Template**
   - Ensure `dashboard.html` has content in `{% block content %}` section

4. **Verify User Shopkeeper Profile**
   - Go to `/admin/` and check if Shopkeeper profile exists for your user

### Issue 7: Database Migrations Failed

**Error:**
```
django.db.migrations.exceptions.MigrationSameNameError
```

**Solution:**

```bash
# Delete migration files (except __init__.py)
# In tracker/migrations/ keep only __init__.py

# Reset migrations
python manage.py makemigrations
python manage.py migrate
```

---

## Common Commands Reference

```bash
# Virtual Environment
python -m venv venv              # Create virtual environment
venv\Scripts\activate            # Activate on Windows
source venv/bin/activate         # Activate on macOS/Linux
deactivate                       # Deactivate environment

# Django Management
python manage.py runserver       # Start development server
python manage.py runserver 8001  # Run on different port
python manage.py makemigrations  # Create migration files
python manage.py migrate         # Apply migrations
python manage.py createsuperuser # Create admin user
python manage.py shell           # Django shell for testing
python manage.py collectstatic   # Collect static files

# Database
python manage.py dbshell         # Access database shell
python manage.py dumpdata        # Export data
python manage.py loaddata        # Import data
```
---

## Future Enhancements

- 📊 Advanced analytics and reporting
- 📱 Mobile app version
- 💬 WhatsApp integration for reminders
- 🔔 SMS/Email notifications
- 📈 Business insights and graphs
- 🔐 Two-factor authentication
- 📋 Invoice generation
- 🔄 Payment integration (Razorpay, Stripe)
- 🎨 Customizable themes
- 📱 Responsive mobile design improvements
   
---

## Quick Start Checklist

- [ ] Python 3.8+ installed
- [ ] XAMPP installed with MySQL
- [ ] Virtual environment created and activated
- [ ] Django 4.2 and mysqlclient installed
- [ ] Django project created
- [ ] templates/ folder created with HTML files
- [ ] MySQL database `dues_tracker_db` created
- [ ] Database configured in settings.py
- [ ] Migrations created (`makemigrations`)
- [ ] Migrations applied (`migrate`)
- [ ] Superuser created (`createsuperuser`)
- [ ] Development server running (`runserver`)
- [ ] Accessed application at http://127.0.0.1:8000/
- [ ] Registration and login working
- [ ] Dashboard displaying correctly

---
