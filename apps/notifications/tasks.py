from celery import shared_task
from .services.email import send_email

@shared_task
def send_notification_email_task(subject, message, recipient_list):
    send_email(subject, message, recipient_list)
