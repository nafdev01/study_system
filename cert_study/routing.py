from django.urls import re_path, path

from glossary.consumers import TermInlineConsumer
from planner.consumers import EventConsumer

urlpatterns = [
    re_path(
        r"ws/term/inline/create/(?P<course_id>\w+)/$",
        TermInlineConsumer.as_asgi(),
    ),
    path("ws/event/", EventConsumer.as_asgi()),
]
