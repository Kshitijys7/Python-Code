from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('<int:courseid>',views.detail,name='details-page'),
    path('', views.first,name='Homepage'),
]
