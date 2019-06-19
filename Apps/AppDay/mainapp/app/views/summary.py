from django.contrib.auth.models import User
from django.views import View
from app.models import *
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import *
from django.http import HttpResponse
from django.core.paginator import Paginator


class InitialView(View):
    def get (self, request, **kwargs):

        if kwargs:
            year = kwargs['season']
        else:
            year = 2019
        m = Matches.objects.filter(season=year)
        paginator = Paginator(m, 8)
        page = request.GET.get('page')
        contacts = paginator.get_page(page)
        return render(request, 'first.html', context={
                          'k': contacts, 'range': range(2008,2020), 'year':year
                               }    )