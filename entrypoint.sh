#!/bin/bash
until python manage.py makemigrations && python manage.py migrate
do
  echo "Try again"
done
gunicorn -c gunicorn_conf.py spinach.wsgi:application
