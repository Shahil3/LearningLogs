# LearnLogs Django Project

Welcome to the LearnLogs Django project! This project is designed to manage your learning logs, allowing you to create topics and entries to track your learning progress. Below, you'll find a brief overview of the project structure, including the files and directories, along with the views implemented in the LearnLogs app.

## Project Structure

- **ll_project**: The main project directory containing project-level settings and configurations.
  - `asgi.py`
  - `wsgi.py`
  - `settings.py`: Configuration file for Django settings.
  - `urls.py`: URL patterns for the entire project.
- **ll_env**: The virtual environment for the project.
- **learnlogs**: The main application directory.
  - **accounts**: The accounts app for user registration and authentication.
    - `views.py`: User registration view.
    - `urls.py`: URL patterns for user registration.
  - **learnLogs**: The LearnLogs app for managing learning logs.
    - `views.py`: Views for handling topics, entries, and user interactions.
    - `urls.py`: URL patterns for LearnLogs app.
    - `models.py`: Model definitions for Topic and Entry.
    - `forms.py`: Form definitions for Topic and Entry.
- `db.sqlite3`: The SQLite database file for the project.
- `manage.py`: Django management script.

## LearnLogs Views

### 1. `index`
- **URL:** `/`
- **Description:** The home page of the LearnLogs app.

### 2. `topics`
- **URL:** `/topics/`
- **Description:** Display all topics owned by the logged-in user.

### 3. `topic`
- **URL:** `/topics/<int:topic_id>/`
- **Description:** Display a single topic and all its entries.

### 4. `del_topic`
- **URL:** `/del_topic/<int:topic_id>/`
- **Description:** Delete a topic.

### 5. `new_topic`
- **URL:** `/new_topic/`
- **Description:** Add a new topic.

### 6. `new_entry`
- **URL:** `/new_entry/<int:topic_id>/`
- **Description:** Add a new entry for a specific topic.

### 7. `edit_entry`
- **URL:** `/edit_entry/<int:entry_id>/`
- **Description:** Edit an existing entry.

### 8. `del_entry`
- **URL:** `/del_entry/<int:entry_id>/`
- **Description:** Delete an entry.

## Accounts Views

### 1. `register`
- **URL:** `/register/`
- **Description:** Register a new user.

## Project Settings

- **LOGIN_REDIRECT_URL:** Redirect URL after successful login.
- **LOGOUT_REDIRECT_URL:** Redirect URL after logout.
- **LOGIN_URL:** URL for the login page.
- **BOOTSTRAP3:** Settings for integrating Bootstrap with the project.

## How to Use

1. Clone the repository.
2. Create a virtual environment (`ll_env`) and activate it.
3. Install project dependencies: `pip install -r requirements.txt`.
4. Run migrations: `python manage.py migrate`.
5. Create a superuser: `python manage.py createsuperuser`.
6. Run the development server: `python manage.py runserver`.
7. Access the admin interface at `http://127.0.0.1:8000/admin/` to add topics and entries.

Feel free to explore and customize the project based on your learning needs!
