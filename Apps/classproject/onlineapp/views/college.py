from django.views import View
from onlineapp.models import *
from django.shortcuts import render
from django.http import HttpResponse

class CollegeView(View):
    def get (self,request,*args,**kwargs):
        if(kwargs):
            s = Student.objects.filter(dropped_out=0,college=College.objects.get(acronym=kwargs['acronym'])).values('name','college__acronym','mocktest1__total').order_by('-mocktest1__total')
            return render(request,'students.html',{'k': s})
        colleges=College.objects.all()

        return render(request,template_name='just.html', context={'k': colleges})