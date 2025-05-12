release: python manage.py migrate
web: web: gunicorn crypto_tracker.asgi:application --worker-class daphne.http.ASGIHTTPWorker
celerworker: celery -A crypto_tracker worker & celery -A crypto_tracker beat -l info & wait -n