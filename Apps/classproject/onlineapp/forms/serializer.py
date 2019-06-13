from django.conf.urls import url
from rest_framework import routers, serializers, viewsets
from onlineapp.models import *

class CollegeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = College
        fields = ['name', 'location', 'acronym', 'contact']