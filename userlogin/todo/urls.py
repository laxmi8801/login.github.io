from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('index',views.index, name='index')
]