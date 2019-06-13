from django.views import View
from rest_framework import permissions, status

from onlineapp.models import *
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from onlineapp.forms.serializer import *

@api_view(['GET', 'PUT' ,'DELETE'])
def college_serializer_col(request, *args, **kwargs):
    if request.method == 'GET':
        colleges = College.objects.get(**kwargs)
        #return HttpResponse(colleges)
        col_data = CollegeSerializer(colleges)
        return Response(col_data.data, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        colleges = College.objects.get(**kwargs)
        colleges.delete()
        return Response({kwargs['acronym']:' got deleted'} ,status=status.HTTP_200_OK)
    if request.method == 'PUT':
        c = College.objects.get(**kwargs)
        colleges = CollegeSerializer(c, data=request.data)
        if colleges.is_valid():
            colleges.save()
            return Response({kwargs['acronym']:' is sucessfully edited'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
