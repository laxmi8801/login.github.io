
from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path, include
from django.conf import settings


from . import views

urlpatterns = [
   #  path('',views.login, name='login'),
   #  path('login',views.login, name='login'),
   #  path('signup', views.signup, name='signup'),
      path('', views.display, name='display'),
   #  path('remove/<username>/',views.remove,name='remove'),
   #  path('update/<username>/',views.update,name='update'),
   # path('logout',views.logout,name=logout)
    
    ]
