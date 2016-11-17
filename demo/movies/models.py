from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Rating(models.Model):
    raw_time = models.IntegerField(null=True)
    timestamp = models.DateTimeField(null=True)
    user = models.ForeignKey(
        User, null=True,
        on_delete=models.SET_NULL
    )
    movie = models.ForeignKey(
        'Movie', null=True,
        on_delete=models.SET_NULL
    )

class Movie(models.Model):
    title = models.CharField(max_length=2000)
    
    @property
    def url(self):
        return reverse('movie-detail', args=[self.pk])
