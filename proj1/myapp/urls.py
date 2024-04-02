from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('student/', StudentView.as_view()),
    # path('myapp/', include('myapp.urls')),
]
