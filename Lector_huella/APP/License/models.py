from django.db import models
from APP.Patient.models import Patients
from APP.Nurse.models import Nurses
from APP.Doctor.models import Doctors
# Create your models here.


class Vaccines(models.Model):
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    Data = models.ForeignKey(Patients, on_delete=models.CASCADE, verbose_name='Datos del paciente',
                             blank=True, null=True)
    Biological = models.CharField(max_length=50, verbose_name='Biologico', null=True, blank=True)
    Dose = models.CharField(max_length=60, verbose_name='Dosis', null=True, blank=True)
    Vaccine_date = models.DateField(verbose_name='Fecha de la vacuna', null=True, blank=True)
    Factory = models.CharField(verbose_name='Fabricante', null=True, blank=True, max_length=50)
    Lot = models.CharField(max_length=50, null=True, blank=True, verbose_name='Lote')
    EPSS=[
        ('S', 'SANITAS'),
        ('N', 'NUEVA EPS'),
        ('F', 'FAMISANAR'),
        ('CP', 'CAPITAL SALUD'),
        ('A', 'ALIANSALUD'),
        ('C', 'COMPENSAR'),
        ('CO', 'COMMEVAEPS'),
        ('SA', 'SALUD TOTAL'),
        ('SU', 'SURA'),
        ('SO', 'SOS'),
        ('FU', 'FUNDACION SALUD MIA'),
    ]
    Eps = models.CharField(max_length=100, choices=EPSS, verbose_name='Ips vacunadora',
                           blank=True, null=True)
    Vaccinator_name = models.ForeignKey(Nurses, on_delete=models.CASCADE,
                                        verbose_name='Nombre del vacunador')


class Growth_and_development(models.Model):
    Date_joined = models.DateTimeField(auto_now_add=True)
    Data = models.ForeignKey(Patients, on_delete=models.CASCADE, null=True, blank=True,
                             verbose_name='Datos del paciente')
    Weight = models.CharField(max_length=3, null=True, blank=True, verbose_name='Peso')
    stature = models.CharField(max_length=3, verbose_name='Estatura', null=True, blank=True)
    IMC = models.CharField(max_length=3, verbose_name='Imc', null=True, blank=True)
    Temperature = models.CharField(max_length=2, verbose_name='Temperatura', null=True, blank=True)
    Pulse = models.CharField(max_length=3, verbose_name='Pulso', null=True, blank=True)
    Breathing_frequency = models.CharField( max_length=3, verbose_name='Frecuencia respiratoria',
                                            null=True, blank=True)
    Blood_pressure = models.CharField(max_length=6, null=True, blank=True,
                                      verbose_name='Presion arterial')
    Doctor_name = models.ForeignKey(Doctors, on_delete=models.CASCADE, verbose_name='Doctor'
                                          , null=True, blank=True)

