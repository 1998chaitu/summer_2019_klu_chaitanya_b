from django.views import View
from onlineapp.forms import AddCollege
from onlineapp.models import *
from django.shortcuts import render,redirect
from django.urls import resolve
from django.http import HttpResponse

class AddCollegeView(View):
    def get(self, request, *args, **kwargs):
        form = AddCollege()
        if kwargs:
            c = College.objects.filter(**kwargs).first()
            form = AddCollege(instance=c)
        return render(request, template_name='add_college.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        if resolve(request.path_info).url_name == 'Delete1':
            c=College.objects.get(acronym=kwargs.get('acronym'))
            c.delete()
            return redirect('colleges')
        if resolve(request.path_info).url_name == 'Edit':
            college = College.objects.filter(acronym=kwargs.get('acronym')).first()
            clg = AddCollege(request.POST, instance=college)
            if clg.is_valid():
                clg.save()
                return redirect('colleges')

        if request.method == "POST":
            form = AddCollege(request.POST)
            if form.is_valid():
                form.save()
            return redirect('colleges')