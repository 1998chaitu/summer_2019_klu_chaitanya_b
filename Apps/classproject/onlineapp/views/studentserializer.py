from django.views import View
from rest_framework import permissions, status

from onlineapp.forms.colserializer import *
from onlineapp.models import *
from django.http import HttpResponse, request
from rest_framework.views import APIView
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from onlineapp.forms.serializer import *
from onlineapp.forms import AddStudent,Marks
from django.shortcuts import render,redirect


class MockTestSerializer(APIView):
    pass

@api_view(['GET', 'POST'])
def student_serializer(request, *args, **kwargs):
    if request.method == 'GET':
        k = College.objects.values('id').filter(acronym=kwargs['acronym'])

        stu = Student.objects.filter(college=k[0]['id']).all()
        stu_data = StudentSerializer(stu, many=True)
        return Response(stu_data.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        c = College.objects.get(**kwargs)
        st = Student(college=c)
        stu = StudentSerializer(st, data=request.data)
        mock = MockSerializer(data=request.data['test'])
        if stu.is_valid() and mock.is_valid():
            stu.save(college=c)
            mock.save(student=st)
            return Response(stu.data, status=status.HTTP_201_CREATED)
        return Response(stu.errors, status=status.HTTP_400_BAD_REQUEST)
