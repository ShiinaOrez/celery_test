from datetime import timedelta
from celery.schedules import crontab

BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'

CELERY_TIMEZONE='Asia/Shanghai'

CELERY_IMPORTS = (
    'celery_app.mail_test',
)

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds' : {
        'task' : 'celery_app.mail_test.send_mail',
        'schedule' : timedelta(seconds=30),
    }
}
