from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from sys import implementation
from .models import Patients


class PatientsSerializer(ModelSerializer):
    class Meta:
        model = Patients
        fields = (
            'id',
            'Name',
            'Surname',
            'age',
            'Cc',
            'Phone',
            'Direction',
            'gender',
            'Eps',
            'email',
            'date_of_birth',)
