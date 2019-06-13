from django.views import View
from rest_framework import permissions, status

from onlineapp.models import *
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from onlineapp.forms.colserializer import *

@api_view(['GET', 'PUT' ,'DELETE'])
def stu_serializer_col(request, *args, **kwargs):
    if request.method == 'GET':
        k = College.objects.values('id').filter(acronym=kwargs['acronym'])
        stu = Student.objects.get(id=kwargs['id'],college=k[0]['id'])
        stu_data = StudentSerializer(stu)
        return Response(stu_data.data, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        k = College.objects.values('id').filter(acronym=kwargs['acronym'])
        stu = Student.objects.get(id=kwargs['id'],college=k[0]['id'])
        stu.delete()
        return Response({kwargs['acronym']:' got deleted'} ,status=status.HTTP_200_OK)
    if request.method == 'PUT':
        k = College.objects.values('id').filter(acronym=kwargs['acronym'])
        s = Student.objects.get(id=kwargs['id'],college=k[0]['id'])
        stu = StudentSerializer(s, data=request.data)
        mocktest = MockSerializer(data=request.data)

        if stu.is_valid():
            stu.save()
            return Response({kwargs['acronym']:' is sucessfully edited'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
