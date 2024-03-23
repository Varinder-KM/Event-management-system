from django.db import models

# Create your models here.
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return str(self.event_name)