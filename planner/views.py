import json

from django.shortcuts import render

from planner.forms import MyEventForm
from planner.models import MyEvent


def calendar_view(request):
    myevents = MyEvent.objects.all()

    form = MyEventForm()

    # make a javascript array of events with the title set to the event name and the start set to the event start time and the end set to the event end time
    myevents_json = [
        {
            "id": myevent.id,
            "title": myevent.name,
            "start": myevent.start_time.strftime("%Y-%m-%dT%H:%M:%S"),
        }
        for myevent in myevents
    ]

    # Convert the list of dictionaries to a JSON string
    myevents_json = json.dumps(myevents_json)

    template_name = "planner/calendar.html"
    context = {
        "myevents": myevents,
        "myevents_json": myevents_json,
        "section": "calendar",
        "form": form,
    }
    return render(request, template_name, context)
