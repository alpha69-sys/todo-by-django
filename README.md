# Todo List Django App

A simple todo list application built with Django and styled with Tailwind CSS.

## Features

- Add tasks to a list
- View all tasks
- Session-based storage (no database persistence)
- Responsive design with Tailwind CSS
- Live reload for development (Django browser reload)

## Setup

1. **Clone or download the project**

2. **Install dependencies:**
   ```
   pip install -r requirement.txt
   ```

3. **Run migrations:**
   ```
   python manage.py migrate
   ```

4. **Install Tailwind CSS:**
   ```
   python manage.py tailwind install
   ```

5. **Build Tailwind CSS:**
   ```
   python manage.py tailwind build
   ```

6. **Run the development server:**
   ```
   python manage.py runserver
   ```

   The app will be available at `http://127.0.0.1:8000/`

## Usage

- **View tasks:** Navigate to the root URL `/` to see the list of tasks.
- **Add a task:** Click "Add a new task" or go to `/add/` to add a new task.

## Development

- For live Tailwind CSS reloading, run `python manage.py tailwind start` in a separate terminal.
- The app uses Django's browser reload for automatic page refreshes on code changes.

## Project Structure

- `todo/`: Main Django project settings
- `todolist/`: Todo list app with models, views, and templates
- `theme/`: Tailwind CSS configuration and static files
- `requirement.txt`: Python dependencies

## Notes

- Tasks are stored in Django sessions, so they will be lost when the session expires.
- Ensure Node.js and npm are installed for Tailwind CSS building.