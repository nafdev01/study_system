# notes/admins.py
from django.contrib import admin
from notes.models import Certification, Domain, Entry

admin.site.register(Certification)
admin.site.register(Domain)
admin.site.register(Entry)
