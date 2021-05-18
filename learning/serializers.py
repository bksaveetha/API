from rest_framework import serializers
from .models import student , depart  ,course

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields  = ('name', 'age', 'email', 'phone')

class departSerializer(serializers.ModelSerializer):
    class Meta:
        model = depart
        fields = ( 'name', 'department', 'year')        

class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model = course
        fields = ('year', 'courses')
  
