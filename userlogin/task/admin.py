from django.contrib import admin
from .models import Todo, Users

# Register your models here
admin.site.register(Todo)
admin.site.register(Users)