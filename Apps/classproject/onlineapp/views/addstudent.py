from django.views import View
from onlineapp.forms import AddStudent,Marks
from onlineapp.models import *
from django.shortcuts import render,redirect
from django.urls import resolve
from django.http import HttpResponse

class AddStudentView(View):
    def get(self, request, *args, **kwargs):
        form = AddStudent()
        form1 = Marks()
        if kwargs:
            pass
        return render(request, template_name='add_student.html', context={'form': form ,'form1': form1  ,
                                                                       'college_name':kwargs.get('acronym')
                                                                       })

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = AddStudent(request.POST)
            form1 = Marks(request.POST)


            if form.is_valid() and form1.is_valid():
                #return HttpResponse(**kwargs)
                c = College.objects.get(**kwargs)
                f = form.save(commit=False)
                form1.save(commit=False)
                f.college = c
                f.save()

                f1 = form1.save(commit=False)
                f1.total = (int(f1.problem1)+int(f1.problem2)+int(f1.problem3)+int(f1.problem4))
                f1.student = Student.objects.get(id=f.id)
                f1.save()
            #return redirect('Students',context={'college_name':kwargs.get('acronym')})
            return redirect('http://127.0.0.1:8000/colleges/'+str(kwargs['acronym'])+'/')