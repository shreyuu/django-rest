from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ApiOverview, name='Home')
]