from django.db import models

# Create your models here.
from APP.Nurse.models import Nurses
from APP.Doctor.models import Doctors
from APP.Patient.models import Patients


class Quotes(models.Model):
    date_and_time = models.DateTimeField()
    doctors = models.ForeignKey(Doctors, on_delete=models.CASCADE, blank=True, null=True,
                                verbose_name='Doctor')
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, blank=True, null=True,
                                verbose_name='Paciente')
    specialitys = [
        ('C Y D','Crecimiento y desarrollo'),
        ('V','Vacunacion'),
    ]
    specialty = models.CharField(max_length=50,choices=specialitys, blank=True, null=True,
                                 verbose_name='consulta')

    def __str__(self):
        return self.patient.Name