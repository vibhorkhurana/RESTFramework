from rest_framework import serializers
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from sensordata.models import Sensor






class sensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields=('id','sensorid','valType','senseVal')
        owner = serializers.ReadOnlyField(source='owner.username')


#     @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


# class sensorSerializer(serializers.HyperlinkedModelSerializer):
#
#     class Meta:
#         model = Sensor
#         fields=('url','id','sensorid','valType','senseVal')
#         owner = serializers.ReadOnlyField(source='owner.username')
#
#
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     sensors = serializers.HyperlinkedRelatedField(many=True, queryset=Sensor.objects.all())
#
#     class Meta:
#         model = User
#         fields = ('url','id', 'username','sensors')
