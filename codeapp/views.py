from http.client import HTTPResponse
from django.shortcuts import render
from .models import *
from .serializers import *
from django.shortcuts import render
import json
from django.shortcuts import render
from rest_framework import serializers
from .models import  *
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.shortcuts import  render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import  api_view, permission_classes,authentication_classes
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,viewsets
from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import ListAPIView
from django_filters.rest_framework  import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from rest_framework import filters

# Create your views here.

class dataApi(APIView):               #data get,delete and post request
    def get(self,request):
        object = itemdata.objects.all()
        serializer = dataSerializer(object,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = dataSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        article = self.get_object(id)
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class datadetail(APIView):     #individual data info get,delete and post request
    def get_object(self,id):
            try:
                return itemdata.objects.get(id = id)
            except itemdata.DoesNotExist:
                return HttpResponse(status = status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        articles = self.get_object(id)
        serializer = dataSerializer(articles)
        return Response(serializer.data)


    def put(self,request,id):
        article  = self.get_object(id)
        serializer = dataSerializer(article,data = request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        article = self.get_object(id)
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class typeApi(APIView):               #type get,delete and post request
    def get(self,request):
        object = itemstype.objects.all()
        serializer = typeSerializer(object,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = typeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        article = self.get_object(id)
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class typefilter(ListAPIView):
        queryset =  itemstype.objects.all()
        serializer_class = typeSerializer
        filter_backends = [DjangoFilterBackend]
        filter_fields = ['types_of_item']

class searchApi(generics.ListCreateAPIView):
    search_fields = ['Name','type','Owner','dateuploaded','Desc','cost']
    filter_backends = (filters.SearchFilter,)
    queryset = itemdata.objects.all()
    serializer_class = dataSerializer