from django.db import models

# Create your models here.
class Sensor(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    sensorid = models.CharField(max_length=100, blank=True,default='')
    valType = models.CharField(max_length=100, blank=True,default='')
    senseVal = models.TextField()

class Meta:
    ordering = ('created',)