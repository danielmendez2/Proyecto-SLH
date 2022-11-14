from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from APP.Nurse.models import Nurses
from APP.Nurse.serializer import NursesSerializer

# Create your views here.


class NursesModelViewSet(ModelViewSet):
    serializer_class = NursesSerializer
    queryset = Nurses.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'put', 'post', 'delete']

