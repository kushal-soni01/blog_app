# Blog App

A simple Django blog application where users can sign up, log in, create posts, upload images, edit their own posts, and delete them.

## Features

- User registration and login
- Create, edit, and delete blog posts
- Image upload for posts
- View all posts or only your own posts
- Admin panel through Django admin

## Tech Stack

- Python
- Django 5
- SQLite for local development
- Bootstrap for UI styling

## Project Structure

```text
blog_app/
|-- blogapp/
|-- blogproject/
|-- manage.py
|-- requirements.txt
|-- Procfile
|-- build.sh
```

## Local Setup

1. Create and activate a virtual environment.
2. Install dependencies.
3. Run migrations.
4. Start the development server.

Example:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open the app in your browser at:

```text
http://127.0.0.1:8000/
```

Important:
Use `http://`, not `https://`, with Django's built-in development server.

## Default Routes

- `/` - home page with posts
- `/signup/` - user registration
- `/accounts/login/` - login
- `/create/` - create a new post
- `/post/<id>/` - post detail page
- `/admin/` - Django admin

## Media and Static Files

- Uploaded images are stored under `media/`
- Static files are served by Django in development

## Deployment Notes

The repository already includes:

- `requirements.txt`
- `build.sh`
- `Procfile`

Before deployment, update the `Procfile` so it points to the correct WSGI app:

```text
web: gunicorn blogproject.wsgi
```

## Useful Commands

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
python manage.py check
```

## License

This project is for learning and personal development use.
