from rest_framework.serializers import ModelSerializer

from .models import History


class HistoriaSerializer(ModelSerializer):
    class Meta:
        model = History
        fields = (
            'id',
            'Name_patients',
            'Occupation',
            'reason_for_consultation',
            'current_illness',
            'hour_entry_finish',
            'Doctor_concept')




