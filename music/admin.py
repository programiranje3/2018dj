from django.contrib import admin

# Register your models here.
from music.models import Performer, Song

admin.site.register(Performer)
admin.site.register(Song)
