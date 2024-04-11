from django.db.models import Model
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('category', 'subcategory','name', 'amount')