from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.viewsets import ViewSet, ModelViewSet
from APP.Patient.models import Patients
from APP.Patient.serializers import PatientsSerializer

# Create your views here.


class PatientsModelViewSet(ModelViewSet):
    serializer_class = PatientsSerializer
    queryset = Patients.objects.all()
    http_method_names = ['get', 'put', 'post', 'delete']
