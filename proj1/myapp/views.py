from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView

# Create your views here.

class StudentView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer