from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, TemplateView
from rest_framework import status
from  rest_framework.views import APIView
from rest_framework.generics import (ListAPIView)
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from .models import History
from .serializers import HistoriaSerializer


class HistoryModelViewSet(ModelViewSet):
    serializer_class = HistoriaSerializer
    queryset = History.objects.all()
    http_method_names = ['get', 'put', 'post', 'delete']