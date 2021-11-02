from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from .models import Users

class form(forms.ModelForm):
    class Meta:
        model = Users
        fields="__all__"