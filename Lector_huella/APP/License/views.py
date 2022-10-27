from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import Vaccines, Growth_and_development
from .serializers import VaccinesSerializer, Growth_and_developmentSerializer


class VaccinesViewSet(ViewSet):
    def list(self, request, *args, **kwargs):
        vaccines = VaccinesSerializer(Vaccines.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=vaccines.data)

    def retrive(self, request, pk: int):
        vaccines = VaccinesSerializer(Vaccines.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=vaccines.data)

    def create(self, request, *args, **kwargs):
        vaccines = VaccinesSerializer(data=request.POST)
        vaccines.is_valid(raise_exception=True)
        vaccines.save()
        return Response(status=status.HTTP_200_OK, data=vaccines.data)


class Growth_and_developmentViewSet(ViewSet):
    def list(self, request, *args, **kwargs):
        growth = Growth_and_developmentSerializer(Growth_and_development.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=growth.data)

    def retrive(self, request, pk: int):
        growth = Growth_and_developmentSerializer(Vaccines.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=growth.data)

    def create(self, request, *args, **kwargs):
        growth = Growth_and_developmentSerializer(data=request.POST)
        growth.is_valid(raise_exception=True)
        growth.save()
        return Response(status=status.HTTP_200_OK, data=growth.data)
