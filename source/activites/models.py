from __future__ import unicode_literals
from django.db import models

class Activity(models.Model):
    event_name = models.CharField(max_length=100, null=False, blank=False)
    event_location = models.CharField(max_length=100, null=False)
    event_address = models.CharField(max_length=100, null=False)
    event_website = models.URLField(null=True)
    event_description = models.TextField(max_length=600, null=True, blank=True)
    event_image = models.URLField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    event_faq = models.TextField(max_length=600, null=True, blank=True)
    phone_number = models.IntegerField(null=True)

    def __unicode__(self):
        return self.event_name

