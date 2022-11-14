from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, TemplateView
from rest_framework import status
from  rest_framework.views import APIView
from rest_framework.generics import (ListAPIView)
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import History
from .serializers import HistoriaSerializer


class HistoryModelViewSet(ModelViewSet):
    serializer_class = HistoriaSerializer
    queryset = History.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'put', 'post', 'delete']