from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.db.models import Count, Avg

# Create your models here.
class Band(models.Model):
    """A model of a rock band."""
    name = models.CharField(max_length=200)
    can_rock = models.BooleanField(default=True)

    @property
    def average_member_age(self):
        agg_qs = self.members.aggregate(average_age=Avg('age'))
        return agg_qs['average_age']

    def get_url(self):
        return reverse('band-detail', args=[self.pk])


class Member(models.Model):
    """A model of a rock band member."""
    name = models.CharField("Member's name", max_length=200)
    instrument = models.CharField(choices=(
            ('g', "Guitar"),
            ('b', "Bass"),
            ('d', "Drums"),
        ),
        max_length=1
    )
    band = models.ForeignKey(
        "Band",
        related_name='members'
    )
    age = models.IntegerField(
        default=24
    )
