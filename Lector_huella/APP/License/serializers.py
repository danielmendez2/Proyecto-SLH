from rest_framework.serializers import ModelSerializer

from .models import Vaccines, Growth_and_development


class VaccinesSerializer(ModelSerializer):
    class Meta:
        model = Vaccines
        fields = ('date_joined',
                  'Data',
                  'Biological',
                  'Dose',
                  'Vaccine_date',
                  'Factory',
                  'Lot',
                  'Eps',
                  'Vaccinator_name',)


class Growth_and_developmentSerializer(ModelSerializer):
    class Meta:
        model = Growth_and_development
        fields = (
            'Date_joined',
            'Data',
            'Weight',
            'stature',
            'IMC',
            'Temperature',
            'Pulse',
            'Breathing_frequency',
            'Blood_pressure',
            'Doctor_name',
        )
