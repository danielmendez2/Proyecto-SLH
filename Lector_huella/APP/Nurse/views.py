from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet
from APP.Nurse.models import Nurses
from APP.Nurse.serializer import NursesSerializer

# Create your views here.


class NursesModelViewSet(ModelViewSet):
    serializer_class = NursesSerializer
    queryset = Nurses.objects.all()
    http_method_names = ['get', 'put', 'post', 'delete']

