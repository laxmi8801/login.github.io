from django.contrib import admin
from .models import Todo,data

# Register your models here
admin.site.register(Todo)
#admin.site.register(Users)

admin.site.register(data)