from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from APP.Nurse.models import Nurses
from APP.Nurse.serializer import NursesSerializer

# Create your views here.


class NurseViewSet(ViewSet):
    def list(self, request):
        nurses = NursesSerializer(Nurses.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=nurses.data)

    def retrive(self, request, pk: int):
        nurses = NursesSerializer(Nurses.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=nurses.data)

    def create(self, request):
        nurses = NursesSerializer(data=request.data)
        nurses.is_valid(raise_exception=True)
        nurses.save()
        return Response(status=status.HTTP_200_OK, data=nurses.data)
