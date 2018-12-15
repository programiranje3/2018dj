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
        return self.name + (' (band)' if self.performer_choices else ' (musician)')

    def get_absolute_url(self):
        return reverse('peformer-detail', args=[str(self.id)])

