from django.shortcuts import render
from planner.models import MyEvent
import json

def calendar_view(request):
    myevents = MyEvent.objects.all()

    # make a javascript array of events with the title set to the event name and the start set to the event date
    myevents_json = [
        {"title": event.name, "start": event.event_on.strftime("%Y-%m-%d")}
        for event in myevents
    ]

    # Convert the list of dictionaries to a JSON string
    myevents_json = json.dumps(myevents_json)

    template_name = "planner/calendar.html"
    context = {
        "myevents": myevents,
        "myevents_json": myevents_json,
        "section": "calendar",
    }
    return render(request, template_name, context)
