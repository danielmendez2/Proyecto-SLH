from rest_framework.serializers import ModelSerializer
from sys import implementation
from .models import Doctors


class DoctorsSerializer(ModelSerializer):
    class Meta:
        model = Doctors
        fields = (
            'id',
            'Photo',
            'Name',
            'Surname',
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
