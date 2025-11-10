# Micro Event Analytics

## Purpose
Tracks user events and displays real-time aggregated counts.

## Stack
Django (backend)
SQLite (storage)
Vanilla JavaScript (frontend)

## Architecture
Browser emits event → POST /event
Django stores event → SQLite
Browser fetches stats → GET /stats
Page updates counts in place

## Endpoints
POST /event
payload: {"type": "<event_name>"}
response: {"status":"ok"}

GET /stats
response: [{"type": "<event_name>", "count": <integer>}]

## Local Setup
python -m venv env
source env/bin/activate
pip install django gunicorn
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

## Deployment Notes
Procfile: web: gunicorn major.wsgi
requirements.txt includes django and gunicorn
ALLOWED_HOSTS contains deployed domain
CSRF_TRUSTED_ORIGINS contains deployed domain
Run migrations after deploy
