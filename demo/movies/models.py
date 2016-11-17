from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Rating(models.Model):
    raw_time = models.IntegerField(null=True)
    timestamp = models.DateTimeField(null=True)