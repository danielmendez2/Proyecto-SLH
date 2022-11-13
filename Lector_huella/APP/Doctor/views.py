
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet
from APP.Doctor.models import Doctors
from APP.Doctor.serializer import DoctorsSerializer

# Create your views here.


class DoctorsModelViewSet(ModelViewSet):
    serializer_class = DoctorsSerializer
    queryset = Doctors.objects.all()
    http_method_names = ['get', 'put', 'post', 'delete']
