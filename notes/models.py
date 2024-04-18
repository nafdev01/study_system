from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


class CommonModel(models.Model):
    """
    Common abstract model for notes application certification, topic,subtopic, and entry.
    """

    name = models.CharField(max_length=250)
    slug = models.SlugField(
        max_length=250,
        null=True,
        blank=True,
        editable=False,
    )
    updated = models.DateTimeField(default=timezone.now, editable=False)

    def get_absolute_url(self):
        return reverse(
            f"{self._meta.verbose_name.lower()}_detail",
            args=[
                self.id,
                self.slug,
            ],
        )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Certification(CommonModel):
    """
    Model for certifications
    """

    student = models.ForeignKey(
        "accounts.Student",
        on_delete=models.CASCADE,
        null=True,
        related_name="certifications",
    )
    abbreviation = models.CharField(max_length=250, default="CODE")
    about = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.abbreviation = self.abbreviation.upper()
        super(Certification, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.abbreviation})"

    class Meta:
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"
        ordering = ["abbreviation"]


class Domain(CommonModel):
    """
    model for certification topic
    """

    certification = models.ForeignKey(
        Certification,
        on_delete=models.CASCADE,
        null=True,
        related_name="domains",
    )
    number = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"{self.number}. {self.name} in {self.certification.abbreviation}"

    class Meta:
        verbose_name = "Domain"
        verbose_name_plural = "Domains"
        ordering = ["certification", "number"]
        unique_together = ["certification", "number"]


class Entry(CommonModel):
    """
    model for domain entry
    """

    domain = models.ForeignKey(
        Domain, on_delete=models.CASCADE, null=True, blank=True, related_name="entries"
    )
    content = models.TextField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entries"
        ordering = ["updated", "name"]
        unique_together = ["name", "domain"]
