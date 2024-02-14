python3 manage.py collectstatic --no-input
python3 manage.py migrate
gunicorn -w 4 -b 0.0.0.0:8000 project.wsgi:application

