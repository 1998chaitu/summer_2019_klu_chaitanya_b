from django.contrib.auth.models import User
from django.views import View
from app.models import *
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import *
from django.http import HttpResponse

class MatchView(View):
    def get(self, request, **kwargs):
        m = Matches.objects.get(id=kwargs['id'])
        d = Deliveries.objects.filter(match_id=m)
        return render(request, 'match.html', {'match': m, 'del': d });