from rest_framework.serializers import ModelSerializer

from .models import Vaccines, Growth_and_development


class VaccinesSerializer(ModelSerializer):
    class Meta:
        model = Vaccines
        fields = (
                  'name_patient',
                  'Biological',
                  'Dose',
                  'Vaccine_date',
                  'Factory',
                  'Lot',
                  'Eps',
                  'Ips',
                  'Vaccinator_name',)


class Growth_and_developmentSerializer(ModelSerializer):
    class Meta:
        model = Growth_and_development
        fields = (

            'name_patients',
            'Weight',
            'stature',
            'IMC',
            'Temperature',
            'Pulse',
            'Breathing_frequency',
            'Blood_pressure',
            'Doctor_name',
        )
