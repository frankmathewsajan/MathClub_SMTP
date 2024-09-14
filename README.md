## Overview

The SMTP Mail project is a web-based email application developed using Django. It allows users to send, receive, and view emails. This project demonstrates basic web development skills, including form handling, state management, and email processing using Django.

## Features

- **Compose Email**: Users can create and send new emails.
- **Inbox**: Users can view received emails.
- **Sent Mail**: Users can view emails they have sent.
- **Email Details**: Users can view the full content of an email.
- **User Authentication**: Users must log in to access their email account.

## Requirements

- Python 3.x
- Django
- HTML/CSS for frontend
- SQLite (or another database) for storing emails

## Installation

### Installation Steps

1. **1. Clone the Repository**
    
    ```bash
    git clone &lt;repository-url&gt;
    cd mail
    ```
    
2. **2. Set Up Virtual Environment**
    
    ```bash
    python -m venv venv
    venv\Scripts\activate # On Linux use `source venv/bin/activate`
    ```
    
3. **3. Install Dependencies**
    
    ```bash
    pip install -r requirements.txt
    ```
    
4. **4. Set Up Database**
    
    ```bash
    python manage.py migrate
    ```
    
5. **5. Login  (Optional)**
    
    You may use `frankmathewsajan@gmail.com` with password `1234567890` for login, or register a user yourself.
    
6. **6. Run the Application**
    
    ```python
    python manage.py runserver
    ```
    
    Access the application at `http://localhost:8000`
    

## Usage

### Compose Email

- Navigate to the "Compose" page.
- Enter the recipient's email address, subject, and message.
- Click "Send" to send the email.

### Inbox

- Navigate to the "Inbox" page.
- View the list of received emails.
- Click on an email to view its details.

### Sent Mail

- Navigate to the "Sent Mail" page.
- View the list of sent emails.
- Click on an email to view its details.

### Email Details

- Click on any email in the inbox or sent mail to view its full content, including sender, recipient, subject, and message.

## Code Structure

- **`manage.py`**: Django's command-line utility for administrative tasks.
- **`mail_project/`**: Directory containing Django project settings and configuration.
    - **`settings.py`**: Configuration settings for the Django project.
    - **`urls.py`**: URL declarations for the project.
    - **`wsgi.py`**: WSGI configuration for the project.
- **`mail/`**: Django app containing the core functionality.
    - **`models.py`**: Contains the data models for the application.
    - **`views.py`**: Contains the view functions that handle requests and responses.
    - **`forms.py`**: Defines forms used in the application.
    - **`templates/`**: Directory containing HTML templates for the frontend.
    - **`static/`**: Directory containing static files like CSS and JavaScript.

## Troubleshooting

- **Issue: Application not running**
    - Ensure that all dependencies are installed.
    - Check if the virtual environment is activated.
    - Verify that the Django development server is running without errors.
- **Issue: Database errors**
    - Ensure that the database is properly set up and migrated.
    - Check the configuration settings for database connection in `settings.py`.