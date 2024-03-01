#!/bin/sh

# Apply migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --no-input

# Start Gunicorn server
exec gunicorn --bind :8000 config.wsgi:application