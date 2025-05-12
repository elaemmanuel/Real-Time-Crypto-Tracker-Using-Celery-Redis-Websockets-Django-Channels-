release: python manage.py migrate
web: web: gunicorn crypto_tracker.asgi:application --worker-class daphne.http.ASGIHTTPWorker
worker: celery -A crypto_tracker worker -l info -B