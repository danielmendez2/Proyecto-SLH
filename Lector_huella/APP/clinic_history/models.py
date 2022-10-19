from django.db import models
from APP.Patient.models import Patients
# Create your models here.


class History(models.Model):
    Name = models.ForeignKey(Patients, on_delete=models.CASCADE, verbose_name='Nombre')
    Rh = models.CharField(max_length=2, verbose_name='Rh')
    Occupation = models.CharField(max_length=100, verbose_name='Ocupacion')
    reason_for_consultation = models.CharField(max_length=1000, verbose_name='Motivo de la consulta')
    current_illness = models.CharField(max_length=100,verbose_name='Enfermdad actual')
    hour_entry_finish = models.DateTimeField(max_length=100, verbose_name='Hora de ingreso')
    Doctor_concept = models.TextField(max_length=1000, verbose_name='Concepto del doctor')

    def __str__(self):
        return self.Name.Name


