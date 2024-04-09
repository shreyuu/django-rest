from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        # fields = ['name', 'age']
        fields = '__all__' 
        # exclude = ['age'] 
        
    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError({'error' : 'age must be above 18'})
        return value
    
    def validate_name(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError({'error' : 'name must not contain numeric'})
        return value
