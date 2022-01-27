from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from task import views


urlpatterns = [
 #   path('',include('task.urls')),
    path('admin/',admin.site.urls),
    url(r'^todo/',views.Todolist.as_view()),
    url(r'^data',views.datalist.as_view()),
    ]

