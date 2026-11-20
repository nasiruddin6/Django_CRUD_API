# Django CRUD API

Django দিয়ে post management ও CRUD (Create, Read, Update, Delete) শেখার একটি practice project।

## বর্তমান অবস্থা

- `post` app এবং `Post` model তৈরি আছে।
- Post-এর `title` ও `content` field আছে।
- SQLite database ব্যবহার করা হয়েছে।
- Django admin route: `/admin/`।
- CRUD API endpoints এখনো implement করা হয়নি।

## পরিকল্পিত features

| HTTP method | কাজ |
| --- | --- |
| GET | Post list ও details দেখা |
| POST | নতুন post তৈরি করা |
| PUT | একটি post পুরোপুরি update করা |
| PATCH | Post-এর নির্দিষ্ট field update করা |
| DELETE | Post মুছে ফেলা |

Frontend থেকে JavaScript-এর `fetch()` দিয়ে API request পাঠানোর পরিকল্পনা আছে। `fetch()` একটি function, HTTP method নয়।

## Project structure

```text
django_crud_api/
├── README.md
├── myprojects/
│   ├── manage.py
│   ├── myprojects/    # Settings ও মূল URL configuration
│   └── post/          # Post app ও migration files
└── venv/              # Local virtual environment
```

## Local setup

Repository root থেকে চালান:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install 'Django>=4.2,<4.3'
cd myprojects
python manage.py migrate
python manage.py runserver
```

Admin page: http://127.0.0.1:8000/admin/

Admin user তৈরি করতে:

```bash
python manage.py createsuperuser
```

Model পরিবর্তন করলে:

```bash
python manage.py makemigrations
python manage.py migrate
```

## GitHub repository

Git commands এই directory থেকে চালান:

```bash
cd /home/nasir/django_projects/django_crud_api
```

এতে `README.md` ও `myprojects/` একই repository-তে থাকবে।
`venv/`, `.env`, `__pycache__/` ও local `db.sqlite3` Git-এ commit করবেন না। Migration files commit করুন।
