from rest_framework import serializers
from sensordata.models import Sensor
class sensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields=('id','sensorid','valType','senseVal')