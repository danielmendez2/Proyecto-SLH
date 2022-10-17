from django.db.migrations import serializer
from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password','is_staff', 'is_active')






