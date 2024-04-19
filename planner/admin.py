from django.contrib import admin
from planner.models import MyEvent


@admin.register(MyEvent)
class MyEventAdmin(admin.ModelAdmin):
    list_display = ["name", "event_on", "category"]
    list_filter = ["category"]
