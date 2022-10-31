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
    def list(self, request):
        history = HistoriaSerializer(History.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=history.data)

    def retrive(self, request, pk: int):
        history = HistoriaSerializer(History.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=history.data)

    def create(self, request):
        history = HistoriaSerializer(data=request.data)
        history.is_valid(raise_exception=True)
        history.save()
        return Response(status=status.HTTP_200_OK, data=history.data)

    def update(self,request):
        history = HistoriaSerializer(History.objects.update(),many=True)
        return Response(status=status.HTTP_200_OK, data=history.data)




#class HistoriaListAPIView(APIView):

 #   def get(self, request,):
  #      historias = HistoriaSerializer(History.objects.all(),many=True)
   #     return Response(status=status.HTTP_200_OK,data=historias.data)

    #def post(self, request, ):
     #   Historias = HistoriaSerializer(data=request.POST)
      #  Historias.is_valid(raise_exception=True)
       # Historias.save()

        #return Response(status=status.HTTP_200_OK, data=Historias.data)