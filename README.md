# CampusConnect – Django Web Application

**Full Name:** [Enter Your Full Name]
**Section:** [Enter Your Section]

## Project Description

CampusConnect is a Django-based web application designed to manage user accounts with role-based access. The system supports three user roles: Student, Instructor, and Administrator. It includes user registration, login, logout, profile management, a dashboard, and an administrator panel accessible only to users assigned the Administrator role.

The project uses Django for its backend, SQLite for its database, and HTML templates with Bootstrap styling for its user interface.

## Steps to Run the Project

### 1. Extract the Project

Download and extract the ZIP file. Open the extracted `Escobanas_campusconnect-main` folder in Visual Studio Code or another code editor or clone it since it is public you can access it

### 2. Open the Terminal

Open a terminal inside the project folder containing the `manage.py` file.

### 3. Create a Virtual Environment

Make sure Python is installed on your computer. Run:

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows Command Prompt:

```bash
.venv\Scripts\activate
```

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Django

Install the Django framework required by the project:

```bash
python -m pip install "Django==6.1.2"
```

### 6. Apply Database Migrations

Initialize the SQLite database and create the required tables by running:

```bash
python manage.py migrate
```

### 7. Create an Administrator Account (Optional)

To create a Django superuser, run:

```bash
python manage.py createsuperuser
```

Enter the required username, email (if requested), and password.

**Note:** A Django superuser does not automatically receive the application's custom `ADMIN` role. Access to the CampusConnect administrator panel requires a user whose role is set to `ADMIN`.

### 8. Start the Development Server

Run the following command:

```bash
python manage.py runserver
```

Once the server starts successfully, open your browser and visit:

**[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

### 9. Access and Test the System

After opening the application:

1. Select Sign Up to create a new user account.
2. Log in using your registered username and password.
3. Access the dashboard after successful authentication.
4. Navigate to your profile to update your personal information.
5. If your account has the `ADMIN` role, access the administrator panel.
6. Log out when finished.
