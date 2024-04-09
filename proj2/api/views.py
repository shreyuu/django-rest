from django.shortcuts import render
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items' : '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
    
    return Response(api_urls)