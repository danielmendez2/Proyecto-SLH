from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from APP.Patient.models import Patients
from APP.Patient.serializers import PatientsSerializer

# Create your views here.


class PatientsViewSet(ViewSet):
    def list(self, request):
        patients = PatientsSerializer(Patients.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=patients.data)

    def retrive(self, request, pk: int):
        patient = PatientsSerializer(Patients.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=patient.data)

    def create(self, request):
        patient = PatientsSerializer(data=request.data)
        patient.is_valid(raise_exception=True)
        patient.save()
        return Response(status=status.HTTP_200_OK, data=patient.data)

    def update(self, request):
        patient = PatientsSerializer(Patients.objects.update(), many=True)
        return Response(status=status.HTTP_200_OK, data=patient.data)
        