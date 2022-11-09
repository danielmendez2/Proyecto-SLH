from django.db import models
from APP.Patient.models import Patients
# Create your models here.


class History(models.Model):
    Name_patients = models.ForeignKey(Patients, on_delete=models.CASCADE, verbose_name='Nombre')
    Rh = models.CharField(max_length=3, verbose_name='Rh', null=True, blank=True)
    Occupation = models.CharField(max_length=100, verbose_name='Ocupacion',null=True, blank=True)
    reason_for_consultation = models.CharField(max_length=1000, verbose_name='Motivo de la consulta',
                                               blank=True, null=True)
    current_illness = models.CharField(max_length=100, verbose_name='Enfermdad actual', null=True, blank=True)
    hour_entry_finish = models.DateTimeField(max_length=100, verbose_name='Hora de ingreso', null=True
                                             , blank=True)
    Doctor_concept = models.TextField(max_length=1000, verbose_name='Concepto del doctor', blank=True, null=True)

    def __str__(self):
        return self.Name_patients.Name


