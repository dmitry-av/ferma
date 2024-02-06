#!/bin/bash

set -e

echo "${0}: running migrations."
python manage.py makemigrations
echo "${0}: running migrations 2"
python manage.py migrate --noinput

echo "${0}: collecting statics."

python manage.py collectstatic --noinput

# gunicorn --bind 0.0.0.0:8000 ferma.wsgi
python ./manage.py runserver 0.0.0.0:8000