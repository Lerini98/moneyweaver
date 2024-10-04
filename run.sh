#!/bin/sh

# Django ORM 적용
python manage.py makemigrations
python manage.py migrate --no-input

# static( css & js ) 적용
python manage.py collectstatic --no-input

# gunicorn을 이용한 django server 구동
gunicorn config.wsgi:application --bind 0.0.0.0:8000 &

# nginx 설정 적용
unlink /etc/nginx/sites-enabled/default

# nginx 실행
nginx -g 'daemon off;'