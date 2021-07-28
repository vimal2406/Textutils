from os import name
from django import urls
from django.contrib.admin.sites import site
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('analyze',views.analyze, name='analyze'),
    path('exe1',views.exe1, name='exe1'),
    
]