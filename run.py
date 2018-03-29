from celery_app import mail_test

mail_test.send_mail.apply_async()

print ('test')
