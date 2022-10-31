from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from sys import implementation
from .models import Nurses


class NursesSerializer(ModelSerializer):
    class Meta:
        model = Nurses
        fields = (
            'id',
            'Photo',
            'Name',
            'Surname',
            'type_identification',
            'identification_number',
            'Phone',
            'Direction',
            'gender',
            'Eps',
            'email',
            'Professional_card',
            'Specialization',
            'date_of_birth',
            'meets_the_profile',
        )
