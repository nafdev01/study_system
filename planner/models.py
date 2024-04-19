from django.db import models
from django.utils import timezone


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

    name = models.CharField(max_length=50)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    added_on = models.DateTimeField(default=timezone.now, editable=False)
    category = models.CharField(
        max_length=2,
        choices=Category.choices,
        default=Category.INFO,
    )

    def __str__(self):
        """Unicode representation of MyEvent."""
        return f"{self.name} from {self.start_time} to {self.end_time}"

    def save(self, *args, **kwargs):
        if self.start_time > self.end_time:
            raise ValueError("Start time must be before end time")
        self.added_on = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "My Event"
        verbose_name_plural = "My Events"
        ordering = ["start_time"]
