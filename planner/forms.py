from django import forms

from planner.models import MyEvent
from planner.widgets import DateTimePickerInput


class MyEventForm(forms.ModelForm):
    class Meta:
        model = MyEvent
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "start_time": DateTimePickerInput(attrs={"class": "form-control"}),
            "end_time": DateTimePickerInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
        }
