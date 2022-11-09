from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (ListAPIView)
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


class UserModelViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    http_method_names = ['get', 'put', 'post', 'delete']


