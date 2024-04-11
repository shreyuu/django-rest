from django_rest import serializers
from .models import TodoItem
from rest_framework import serializers


class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = "__all__"