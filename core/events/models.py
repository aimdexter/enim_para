from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=30)
    event_location = models.CharField(max_length=30)
    def __str__(self):
        return self.event_name