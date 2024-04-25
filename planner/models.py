from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from planner.tasks import send_email_task


class MyEvent(models.Model):
    """Model definition for MyEvent."""

    # choices for reasons for a ban

    class Category(models.TextChoices):
        SUCCESS = "SC", "Sucess"
        DANGER = "DG", "Danger"
        INFO = "IN", "Info"
        PINK = "PN", "Pink"
        PRIMARY = "PR", "Primary"
        WARNING = "WR", "Warning"

    student = models.ForeignKey(
        "accounts.Student",
        on_delete=models.CASCADE,
        related_name="events",
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=50)
    start_time = models.DateTimeField(default=timezone.now)
    added_on = models.DateTimeField(default=timezone.now, editable=False)
    category = models.CharField(
        max_length=2,
        choices=Category.choices,
        default=Category.INFO,
    )

    def __str__(self):
        """Unicode representation of MyEvent."""
        return f"{self.name} from {self.start_time}"

    def save(self, *args, **kwargs):
        self.added_on = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "My Event"
        verbose_name_plural = "My Events"
        ordering = ["start_time"]


@receiver(post_save, sender=MyEvent)
def event_notification(sender, instance, created, **kwargs):
    if created:
        # Schedule the task to run at the event's start time
        send_email_task.apply_async(args=[
            instance.name,
            instance.student.email,
            instance.start_time,
        ], eta=instance.start_time)
