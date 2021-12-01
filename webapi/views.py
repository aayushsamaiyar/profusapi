# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import items, categories
from .serializers import categoriesSerializer, itemSerializer

# Create your views here.

class categoriesList(APIView):
   def get(self, request):
      categories1 = categories.objects.all()
      serializer = categoriesSerializer(categories1, many=True)

      return Response(serializer.data)
   
   def post(self):
      pass

class itemList(APIView):

   def get(self, request, myid):
      item1 = items.objects.filter(cate_id = myid)

      serializer = itemSerializer(item1,many=True)
      return Response(serializer.data)

class itemView(APIView):
   def get(self, request, myid):
      query = request.GET.get('item_id')
      item1 = items.objects.filter(item_id = myid)
      serializer = itemSerializer(item1,many=True)

      return Response(serializer.data)

