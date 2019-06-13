from django.views import View
from rest_framework import permissions, status

from onlineapp.models import *
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from onlineapp.forms.serializer import *

@api_view(['GET', 'POST'])
#@permission_classes(permissions.AllowAny)
def college_serializer(request, *args, **kwargs):
    if request.method == 'GET':
        colleges = College.objects.all()
        col_data = CollegeSerializer(colleges,many=True)
        return Response(col_data.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        colleges = CollegeSerializer(data=request.data)
        if colleges.is_valid():
            colleges.save()
            return Response(colleges.data, status=status.HTTP_201_CREATED)
        return Response(colleges.errors, status=status.HTTP_400_BAD_REQUEST)
