from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.exceptions import *

# Create your views here.

@api_view(['GET'])
def myapp(request):
    student_objs = student.objects.all()
    serializer = StudentSerializer(student_objs, many=True)
    return Response({'status' : 200 , 'payload' : serializer.data})

@api_view(['POST'])
def post_student(request):
    data = request.data
    serializer = StudentSerializer(data = request.data)
    
    if not serializer.is_valid():
        print(serializer.errors)
        print(serializer.errors)
        raise ValidationError(serializer.errors)
        return Response({'status' : 403, "errors" : serializer.errors, 'message' : 'something went wrong'})
    serializer.save()
    
    return Response({'status' : 200 , 'payload' : serializer.data , 'message' : 'you sent'})
