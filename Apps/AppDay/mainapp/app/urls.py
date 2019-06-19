from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls import include, url  # For django versions before 2.0
from django.urls import include, path  # For django versions from 2.0 and up
from app.views import *



urlpatterns = [
    path('summary/<int:season>/<int:id>/login/', LoginView.as_view(), name="login1"),
    path('signup/', SignupView.as_view(), name='signup1'),
    path('summary/', InitialView.as_view()),
    path('summary/<int:season>/', InitialView.as_view(), name='base'),
    path('summary/<int:season>/<int:id>/', MatchView.as_view(), name='Details'),
]

# urlpatterns += [
#     url('api-auth-token/', CustomAuthToken.as_view(), name='xyz')
# ]