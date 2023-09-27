from django.db import models
from django.urls import reverse
# Create your models here.

INSTRUMENTS = (
    ('v', 'Vocals'),
    ('g', 'Guitar'),
    ('b', 'Bass'),
    ('d', 'Drums'),
    ('k', 'Keys'),
    ('o', 'Other')
)

class Award(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('awards_detail', kwargs={'pk': self.id})

class Band(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    awards = models.ManyToManyField(Award)

    def __str__(self):
        return f'{self.name}, ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'band_id': self.id})
    
    def band_length(self):
        return self.musician_set.all().count()
    
class Musician(models.Model):
    name = models.CharField()
    instrument = models.CharField(
        'Primary Instrument',
        max_length=1,
        choices=INSTRUMENTS,
        default=INSTRUMENTS[0][0]
    )
    band = models.ForeignKey(
        Band,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f'{self.name} plays {self.get_instrument_display()}'