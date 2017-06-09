from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.lexers import get_all_lexers
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


LEXERS = [item for item in get_all_lexers() if item[1]]
# Create your models here.
class Sensor(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    sensorid = models.CharField(max_length=100, blank=False,default='')
    valType = models.CharField(max_length=100, blank=False,default='')
    senseVal = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='sensors', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        sensorid = self.sensorid and {'sensorid': self.sensorid} or {}
        valType = self.valType and {'valType': self.valType} or {}
        senseVal = self.senseVal and {'senseVal': self.senseVal} or {}
        super(Sensor, self).save(*args, **kwargs)

class Meta:
    ordering = ('created',)