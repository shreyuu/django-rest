from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', myapp),
    path('student/', post_student)
]