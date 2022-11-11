from django.contrib.auth.models import User
from celery import shared_task
from django.core.mail import send_mail
from Project import settings


@shared_task(bind=True)
def send_mail_fun(self):
    users=User.objects.all()
    for user in users:
        mail_subject=f'Hi!!,Testing {user.first_name}'
        mail_message='This is just testing message from celery project'
        to_email=user.email
        send_mail(
            subject=mail_subject,
            message=mail_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "All mails sent by celery"