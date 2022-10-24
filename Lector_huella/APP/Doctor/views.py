
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from APP.Doctor.models import Doctors
from APP.Doctor.serializer import DoctorsSerializer

# Create your views here.


class DoctorsViewSet(ViewSet):
    def list(self, request):
        doctors = DoctorsSerializer(Doctors.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=doctors.data)

    def retrive(self, request, pk: int):
        doctors = DoctorsSerializer(Doctors.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=doctors.data)

    def create(self, request):
        doctors = DoctorsSerializer(data=request.POST)
        doctors.is_valid(raise_exception=True)
        doctors.save()
        return Response(status=status.HTTP_200_OK, data=doctors.data)

