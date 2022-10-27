from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, TemplateView
from rest_framework import status
from  rest_framework.views import APIView
from rest_framework.generics import (ListAPIView)
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import History
from .serializers import HistoriaSerializer




class HistoryViewSet(ViewSet):
    def list(self, request, *args, **kwargs):
        doctors = HistoriaSerializer(History.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=doctors.data)

    def retrive(self, request, pk: int):
        doctors = HistoriaSerializer(History.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=doctors.data)

    def create(self, request, *args, **kwargs):
        doctors = HistoriaSerializer(data=request.POST)
        doctors.is_valid(raise_exception=True)
        doctors.save()
        return Response(status=status.HTTP_200_OK, data=doctors.data)



#class HistoriaListAPIView(APIView):

 #   def get(self, request,):
  #      historias = HistoriaSerializer(History.objects.all(),many=True)
   #     return Response(status=status.HTTP_200_OK,data=historias.data)

    #def post(self, request, ):
     #   Historias = HistoriaSerializer(data=request.POST)
      #  Historias.is_valid(raise_exception=True)
       # Historias.save()

        #return Response(status=status.HTTP_200_OK, data=Historias.data)