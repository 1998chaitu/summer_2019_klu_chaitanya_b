from django.conf.urls import url
from rest_framework import routers, serializers, viewsets
from onlineapp.models import *

class MockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MockTest1
        fields = ['problem1', 'problem2', 'problem3', 'problem4', 'total' ]

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'email', 'db_folder']