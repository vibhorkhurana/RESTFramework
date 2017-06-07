from django.shortcuts import render
import json
from rest_framework.renderers import JSONRenderer
from sensordata.models import Sensor
from sensordata.serializers import sensorSerializer
from rest_framework import mixins
from rest_framework import generics

def index(request):
    sensors = Sensor.objects.all()
    serializer = sensorSerializer(sensors, many=True)
    json1 = JSONRenderer().render(serializer.data)
    sensie = json.loads(json1)
    return render(request, 'sensorstats/index.html', {
        'sensors': sensie,
    })

class SensorList(generics.ListCreateAPIView):
    queryset=Sensor.objects.all()
    serializer_class=sensorSerializer

class SensorDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a sensor instance
    """
    queryset=Sensor.objects.all()
    serializer_class=sensorSerializer
