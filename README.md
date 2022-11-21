# DjangoCelery
# Configure env file in Project dir
this will use only google mail smtp
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
# Celery Commands**************************

celery -A Project_name.celery worker --beat -l info
celery -A Project_name.celery worker -l info
celery -A Project_name.celery beat -l info

celery -A auto_user.celery worker -l info --concurrency=5  --pool=gevent
