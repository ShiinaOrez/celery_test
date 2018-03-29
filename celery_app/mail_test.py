from flask import Flask,json
from flask_mail import Mail,Message
from celery import Celery
from celery_app import c
import time

app=Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEBUG'] = True
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME'] = 'XXX@qq.com'
app.config['MAIL_PASSWORD'] = "XXX"

#app.config['CELERY_BROKER_URL']='redis://localhost:6379/0'
#app.config['CELERY_RESULT_BACKEND']='redis://localhost:6379/1'

mails=Mail(app)
#celery=Celery('mails',broker=app.config['CELERY_BROKER_URL'])
#celery.conf.update(app.config)
#celery.config_from_object('celery_config')

#celery.conf.beat_schedule = {
#    'add-every-30-seconds': {
#        'task': 'mails.setup_mail_tasks',
#        'schedule': 30.0,
#    },
#}
#celery.conf.timezone = 'UTC'

def test():
    send_mail.apply_async(countdown=10)

@c.task
def send_mail(**kwargs):
    with app.app_context():
        subject="shiina's mail test!"
        body="hello,KOF"
        recipients=["XXX@qq.com"]
        mails.send(maketh_msg(subject,body,recipients))

def maketh_msg(subject,body,r):
    msg=Message(
               subject=subject,
               body=body,
               recipients=r
           )
    return msg

#@celery.on_after_configure.connect
#def setup_mail_tasks(sender, **kwargs):
#    sender.add_periodic_task(10.0,send_mail.s())


if __name__ == '__main__':
    app.run()
