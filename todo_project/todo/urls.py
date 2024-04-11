from django.contrib import admin
from .views import TodoListCreate, TodoDetail
from django.urls import path, include 

urlpatterns = [
        path("todos/", TodoListCreate.as_view(), name='todo-list-create'),
        path("todos/<int:pk>", TodoDetail.as_view(), name='todo-detail')
        
]
