from django.contrib import admin
from django.urls import path , include
from . import views
from rest_framework import routers 


router = routers.DefaultRouter()
router.register('student', views.studentView)
router.register('depart', views.departView)
router.register('course', views.courseView)


urlpatterns = [
    
    path('', include(router.urls))
]