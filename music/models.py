import datetime
from time import strftime

from django.db import models

# Create your models here.
from django.db.models import CharField, BooleanField
from django.urls import reverse


class Performer(models.Model):

    performer_choices = [
        [True, 'band'],
        [False, 'musician'],
    ]

    name = CharField(max_length=100)
    is_band = BooleanField(verbose_name='Band/Musician',
                           choices=performer_choices,
                           default=False)

    def __str__(self):
        return self.name + (' (band)' if self.is_band else ' (musician)')

    def get_absolute_url(self):
        return reverse('performer-detail', args=[str(self.id)])


class Song(models.Model):

    title = models.CharField(max_length=100)
    performer = models.ForeignKey(Performer, on_delete=models.SET_NULL, blank=True, null=True)
    time = models.TimeField(blank=True, null=True, default=datetime.time(minute=3, second=0))
    release_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title + '\n' + \
               '\tperformer: ' + str(self.performer) + '\n' + \
               '\ttime: ' + self.format_time() + '\n' + \
               '\treleased: ' + self.format_date()

    def format_time(self):
        return self.time.strftime('%#M:%S') if isinstance(self.time, datetime.time) else 'unknown'

    def format_date(self):
        return self.release_date.strftime('%b %d, %Y') if isinstance(self.release_date, datetime.date) else 'unknown'

    def get_absolute_url(self):
        return reverse('song-detail', args=[str(self.id)])

