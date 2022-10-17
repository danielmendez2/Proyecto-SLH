from django.db.migrations import serializer
from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'password', 'email')

    def create (self,validate_data):
        user = User(**validate_data)
        user.set_password(validate_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user


class UserListSerializer(ModelSerializer):
    class Meta:
        models: User

    def to_representation(self, instance):
        return {
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password']
        }