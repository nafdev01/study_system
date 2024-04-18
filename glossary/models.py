# glossary/models.py
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from notes.models import Certification, CommonModel


class Term(CommonModel):
    """
    model for important terms in certifications
    """

    certification = models.ForeignKey(
        Certification, on_delete=models.CASCADE, null=True, related_name="terms"
    )
    definition = models.TextField()

    def get_absolute_url(self):
        return reverse(
            f"terms_by_certification",
            args=[
                self.certification.id,
                self.certification.slug,
            ],
        )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Term"
        verbose_name_plural = "Terms"
        ordering = ["name"]
        unique_together = ["certification", "name"]
