from django.db import models

# Create your models here.


class Patients(models.Model):
    Name = models.CharField(max_length=50, verbose_name='Nombre')
    Surname = models.CharField(max_length=50, verbose_name='Apellidos')
    age = models.CharField(max_length=3, verbose_name='Edad')
    Cc = models.CharField(unique=True, max_length=11, verbose_name='Cedula')
    Phone = models.CharField(max_length=13, verbose_name='Telefono')
    Direction = models.CharField(max_length=50, verbose_name='Direccion')
    genders = [
        ('F', 'FEMENINO'),
        ('M', 'MASCULINO'),
        ('O', 'OTRO')
    ]
    gender = models.CharField(max_length=1, choices=genders, verbose_name='Genero')
    EPSS = [
        ('S','SANITAS'),
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
    Eps = models.CharField(max_length=50, choices=EPSS, verbose_name='Eps')
    email = models.EmailField(max_length=100, verbose_name='Correo')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Fecha de cumpleaños')

    def __str__(self):
        return self.Name
