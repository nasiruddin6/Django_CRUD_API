# Django CRUD API

A Django practice project for building a post management API.

## Current Features

- Post model with `title` and `content` fields
- SQLite database
- Django admin route at `/admin/`

## Planned Features

CRUD endpoints using GET, POST, PUT, PATCH, and DELETE, with frontend requests using JavaScript `fetch()`.

## Setup

Run from the repository root:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install 'Django>=4.2,<4.3'
cd myprojects
python manage.py migrate
python manage.py runserver
```

## Structure

```text
django_crud_api/
├── README.md
└── myprojects/
    ├── manage.py
    ├── myprojects/
    └── post/
```

Run Git commands from `django_crud_api/`. Exclude virtual environments, `.env`, Python caches, and local databases from commits.
