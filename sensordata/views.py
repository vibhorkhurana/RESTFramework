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


def index(request):
    sensors = Sensor.objects.all()
    serializer = sensorSerializer(sensors, many=True)
    json1 = JSONRenderer().render(serializer.data)
    sensie = json.loads(json1)
    return render(request, 'sensorstats/index.html', {
        'sensors': sensie,
    })

class SensorList(APIView):
    #@csrf_exempt
    # @api_view(['GET','POST'])
    # def sensor_data(request,format=None):
    #     """
    #     List all sensor data.
    #     """
    #     if request.method == 'GET':
    #         sensors = Sensor.objects.all()
    #         serializer = sensorSerializer(sensors,many=True)
    #         return Response(serializer.data)
    #     elif request.method == 'POST':
    #         serializer = sensorSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data,status=status.HTTP_201_CREATED)
    #         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,format=None):
        sensors=Sensor.objects.all()
        serializer = sensorSerializer(sensors, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = sensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class SensorDetail(APIView):
    """
    Retrieve, update or delete a sensor instance
    """
    def get_sensor(self,pk):
        try:
            return Sensor.objects.get(pk=pk)
        except Sensor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        sensor = self.get_sensor(pk)
        serializer = sensorSerializer(sensor, many=False)
        return Response(serializer.data)

    def put(self,request, pk, format=None):
        sensor = self.get_sensor(pk)
        serializer = sensorSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        sensor = self.get_sensor(pk)
        sensor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

