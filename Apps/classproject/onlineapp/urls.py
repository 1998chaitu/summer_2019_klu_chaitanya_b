from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls import include, url  # For django versions before 2.0
from django.urls import include, path  # For django versions from 2.0 and up
from onlineapp import views
from onlineapp.views import CollegeView,AddCollegeView
from onlineapp.views import AddStudentView,LoginView,SignupView, log_out
from onlineapp.views import *



urlpatterns = [
    path('logout/', log_out, name="logout"),
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignupView.as_view(), name="signup"),

    #path('colleges/<str:acronym>/adds/',)

    path('colleges/', CollegeView.as_view(),name="colleges"),
    path('colleges/<str:acronym>/', CollegeView.as_view(), name = 'Students'),
    path('college/add/', AddCollegeView.as_view(), name = 'Add'),

    path('colleges/<str:acronym>/add/', AddStudentView.as_view(), name='AddS'),
    #path('colleges/<str:acronym>/edit/<int:id>/', AddStudentView.as_view(), name='EditS'),
    #path('colleges/<str:acronym>/del/<int:id>/', AddStudentView.as_view(), name='DeleteS'),

    path('colleges/edit/<str:acronym>/', AddCollegeView.as_view(), name='Edit'),
    path('colleges/del/<str:acronym>/', AddCollegeView.as_view(), name='Delete1'),

    path('api/v1/colleges/', college_serializer, name='s_col'),

    path('api/v1/colleges/<str:acronym>/', college_serializer_col, name='s_col_s'),

    path('api/v1/colleges/<str:acronym>/students/', student_serializer, name='s_stu'),

    path('api/v1/colleges/<str:acronym>/students/<int:id>/', stu_serializer_col, name='s_stu_s'),
]