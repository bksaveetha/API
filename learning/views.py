from django.shortcuts import render
from rest_framework import viewsets
from .models import student , depart  , course
from  .serializers import studentSerializer , departSerializer , courseSerializer 

class studentView(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentSerializer

class departView(viewsets.ModelViewSet):
    queryset = depart.objects.all()
    serializer_class = departSerializer

class courseView(viewsets.ModelViewSet):
    queryset = course.objects.all()
    serializer_class = courseSerializer
   