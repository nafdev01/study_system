# notes/forms.py
from django.utils.translation import gettext_lazy as _
from django import forms
from notes.models import Course, Domain, Entry


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["name", "abbreviation", "about"]
        widgets = {
            "about": forms.Textarea(attrs={"cols": "40", "rows": "4"}),
        }


class DomainForm(forms.ModelForm):
    class Meta:
        model = Domain
        fields = ["number", "name"]


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["name", "content"]
