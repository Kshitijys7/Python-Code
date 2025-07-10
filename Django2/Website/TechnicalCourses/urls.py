from django.contrib import admin

from django.urls import path
from . import views

app_name='TechnicalCourses'

urlpatterns = [
    path('<int:course_id>/',views.detail,name='Details Page'),
    path('', views.Courses,name='Homepage'),
    path('<int:course_id>/yourchoice/',views.yourchoice, name='yourchoice'),
]
