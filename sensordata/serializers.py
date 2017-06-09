from rest_framework import serializers
from django.contrib.auth.models import User


from sensordata.models import Sensor

class sensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields=('id','sensorid','valType','senseVal')
        owner = serializers.ReadOnlyField(source='owner.username')

class UserSerializer(serializers.ModelSerializer):
    sensors = serializers.PrimaryKeyRelatedField(many=True, queryset=Sensor.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'sensors')