from django.shortcuts import render
#from django.shortcuts import render_to_response
import json
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
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

class SensorList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset=Sensor.objects.all()
    serializer_class=sensorSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class SensorDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
    Retrieve, update or delete a sensor instance
    """

    queryset=Sensor.objects.all()
    serializer_class=sensorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

