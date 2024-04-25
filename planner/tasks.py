from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone


@shared_task(name="send_email_task")
def send_email_task(name, email, start_time):
    send_mail(
        subject=f"It's time for {name}",
        message=f"This is a reminder that {name} is starting now ({start_time}). Its important to keep to your schedule and follow your plan for maximum productivity.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[f"{email}"],
        fail_silently=False,
    )
    print(f"Email sent to {email} for {name} at {start_time}")
