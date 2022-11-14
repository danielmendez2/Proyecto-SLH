from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Vaccines, Growth_and_development
from .serializers import VaccinesSerializer, Growth_and_developmentSerializer


class VaccinesModelViewSet(ModelViewSet):
    serializer_class = VaccinesSerializer
    queryset = Vaccines.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'put', 'post', 'delete']


class Growth_and_developmentModelViewSet(ModelViewSet):
    serializer_class = Growth_and_developmentSerializer
    queryset = Growth_and_development.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'put', 'post', 'delete']
