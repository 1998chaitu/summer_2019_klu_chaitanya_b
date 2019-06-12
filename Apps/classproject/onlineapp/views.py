from django.shortcuts import render
from . import views
from django.http import HttpResponse
from . import models


# Create your views here.

def stu(request, acronym):
    c = models.Student.objects.filter(college=models.College.objects.get(acronym=acronym)).values('name', 'college__acronym')
    return render(request, 'students.html', {'k': c})
    # return HttpResponse(c)


def hello(request):
    c = models.College.objects.values('name', 'acronym')

    return render(request, 'just.html', {'k': c})
