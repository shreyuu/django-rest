from django.shortcuts import render
from rest_framework import generics
from .models import TodoItem
from .serializers import ToDoItemSerializer


# Create your views here.


class TodoListCreate(generics.ListCreateAPIView):
    queryset= TodoItem.objects.all()
    serializer_class = ToDoItemSerializer
    
class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= TodoItem.objects.all()
    serializer_class = ToDoItemSerializer