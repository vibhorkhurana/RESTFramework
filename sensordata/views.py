from django.shortcuts import render
import json
from rest_framework.renderers import JSONRenderer
from sensordata.models import Sensor
from sensordata.serializers import sensorSerializer
from sensordata.serializers import UserSerializer
from sensorstats.permissions import IsOwnerOrReadOnly
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view

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
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SensorDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a sensor instance
    """
    queryset=Sensor.objects.all()
    serializer_class=sensorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer