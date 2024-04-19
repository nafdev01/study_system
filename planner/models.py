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
    event_on = models.DateField(auto_now=False, auto_now_add=False)
    added_on = models.DateTimeField(default=timezone.now)
    category = models.CharField(
        max_length=2,
        choices=Category.choices,
        default=Category.INFO,
    )

    def __str__(self):
        """Unicode representation of MyEvent."""
        return f"{self.name} on {self.event_on}"

    class Meta:
        verbose_name = "My Event"
        verbose_name_plural = "My Events"
        ordering = ["event_on"]
