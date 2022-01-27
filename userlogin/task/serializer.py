from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Todo, data

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

# class options(object):
#     def __init__(self, choices, multiplechoices):
#         self.choices = choices
#         self.multiplechoices = multiplechoices

# THE_CHOICES=( 
#     ("1", "One"), 
#     ("2", "Two"), 
#     ("3", "Three"), 
#     ("4", "Four"), 
#     ("5", "Five"), 
# )

class dataSerializers(serializers.ModelSerializer):
    # choices = serializers.ChoiceField(choices=THE_CHOICES)
    # multiplechoices = serializers.MultipleChoiceField(choices=THE_CHOICES)
    class Meta:
        model = data
        fields = '__all__'