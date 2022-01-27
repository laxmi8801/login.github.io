from django.db import models
from django.db.models.fields import EmailField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator



# class Users(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     address = models.CharField(max_length=1024,blank=True,null=True)

#     def __str__(self):
#         return self.user.username


class Todo(models.Model):
    title=models.CharField(max_length=100)
    Description=models.TextField()

    def __str__(self):
        return self.title

class data(models.Model):
#     THE_CHOICES=[
#     ("1", "One"), 
#     ("2", "Two"), 
#     ("3", "Three"), 
#     ("4", "Four"), 
#     ("5", "Five"), 
#     ]
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
  #  choices = THE_CHOICES
    min = models.IntegerField(validators=[ MinValueValidator(1)])#1 or grater
    max = models.IntegerField(validators=[ MinValueValidator(2)])#2
    pincode = models.TextField()


    def __str__(self):
        return self.name
    


