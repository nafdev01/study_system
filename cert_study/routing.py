from django.urls import re_path

from glossary.consumers import TermInlineConsumer

urlpatterns = [
    re_path(r"ws/term/inline/create/(?P<certification_id>\w+)/$", TermInlineConsumer.as_asgi()),
]
