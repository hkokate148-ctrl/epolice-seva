# 🚔 ePolice Seva – Online Police Service Portal

## 📌 About the Project

**ePolice Seva** is a web-based police service portal developed using Django and Python. It provides an online platform where citizens can register, submit complaints, track complaint status, and access important police and legal services.

The main objective of this project is to make police services more accessible, convenient, and user-friendly through a digital platform.

## ✨ Features

### 👤 1. User Authentication

* User Registration and Login
* Secure Password Authentication
* Forgot Password System using OTP
* Password Reset Functionality
* User Profile Management

### 📝 2. Complaint Management System

* Submit complaints online
* Enter incident details and location
* Upload supporting evidence files
* Generate a unique Complaint ID
* Track complaint status online

### 📊 3. Complaint Status Tracking

* Search complaints using a Complaint ID
* View the current complaint status
* Follow the complaint progress

**Complaint Statuses:**

* Submitted
* Under Review
* Investigation
* Resolved

### 👮 4. Staff Portal

* Separate staff login
* View submitted complaints
* Open complaint details
* Update complaint status
* Manage the complaint review process

### 🔐 5. Forgot Password System

* Request a password reset
* Receive an OTP through email
* Verify the OTP
* Create a new password

### 🚨 6. Emergency Services

* Access important emergency contact information
* Find relevant police and assistance services

### ⚖️ 7. Court and Legal Assistance

* Access court-related information
* Explore legal assistance information

### 🛠️ 8. Admin Panel

* Manage users and complaints
* View and manage database records
* Access registered application models
* Manage administrative data through Django Admin

## 🛠️ Technologies Used

| Technology   | Purpose                |
| ------------ | ---------------------- |
| Python       | Backend Programming    |
| Django       | Web Framework          |
| SQLite       | Database               |
| HTML5        | Web Page Structure     |
| CSS3         | Styling                |
| Bootstrap 5  | Responsive UI Design   |
| JavaScript   | Frontend Interactivity |
| Django ORM   | Database Operations    |
| SMTP Email   | OTP Email Delivery     |
| Git & GitHub | Version Control        |

## 📂 Project Structure

```text
ePolice-Seva/
│
├── manage.py
├── my_project1/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   │   └── img/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── apps.py
│
├── templates/
├── static/
├── media/
├── db.sqlite3
└── README.md
```

*Note: The folder structure above is illustrative. Adjust it to match the actual files and folders in your repository.*

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the Project Folder

```bash
cd ePolice-Seva
```

Use the actual folder name created after cloning if it differs.

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### Step 5: Install Django

```bash
pip install django
```

Install any additional dependencies required by the project.

### Step 6: Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 7: Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the instructions to create an administrator account.

### Step 8: Run the Development Server

```bash
python manage.py runserver
```

Open the following address in your browser:

```text
http://127.0.0.1:8000/
```

## 🗄️ Database Models

The project uses Django models to store and manage application data.

* **User:** Manages user authentication and account information.
* **Complain:** Stores complaint details, incident information, evidence, and complaint status.
* **Contact:** Stores contact form submissions.

The Django ORM is used to interact with the database.

## 🔄 How the System Works

1. A citizen registers or logs in.
2. The citizen submits a complaint.
3. The system generates a unique Complaint ID.
4. The citizen uses the ID to check complaint status.
5. Authorized staff review complaints and update their status.
6. The citizen can check the latest status online.

## 🔒 Security

* Django authentication is used for user login.
* Passwords are managed through Django's password-handling system.
* Login protection restricts access to authorized pages.
* Staff permissions control access to complaint-management features.
* OTP verification supports the password-reset process.

**Important:** Configure environment variables for sensitive settings, use secure email credentials, and enable HTTPS before deploying the application publicly. Never upload passwords, email app passwords, or production secret keys to GitHub.

## 🎯 Project Objectives

* Digitize the complaint submission process.
* Make complaint tracking easier for citizens.
* Improve access to police-related information.
* Provide staff with a centralized complaint-management portal.
* Learn and demonstrate practical Django web development.

## 🚀 Future Enhancements

* Multilingual support (Hindi and English).
* Interactive map-based location services.
* More emergency assistance features.
* SMS notifications for complaint updates.
* Advanced complaint analytics and reporting.
* Improved accessibility and mobile responsiveness.

## 👨‍💻 Developer

**Hemant Kokate**

B.Tech Computer Science Engineering Student

**Project:** ePolice Seva – Online Police Service Portal

## 📄 License

This project is developed for educational and learning purposes. Add an appropriate open-source license if you intend to distribute or reuse the code publicly.
