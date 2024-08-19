# notes/admins.py
from django.contrib import admin
from notes.models import Course, Domain, Entry, EntryImage

admin.site.register(Course)
admin.site.register(Domain)
admin.site.register(Entry)
admin.site.register(EntryImage)
