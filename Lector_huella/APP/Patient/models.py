from django.db import models

# Create your models here.


class Patients(models.Model):
    Name = models.CharField(max_length=50, verbose_name='Nombre')
    Surname = models.CharField(max_length=50, verbose_name='Apellidos')
    type_identification = models.CharField(max_length=30, null=True, blank=True, verbose_name='tipo de identificacion')
    identification_number = models.CharField(unique=True, max_length=11, verbose_name='Cedula')
    Phone = models.CharField(max_length=18, verbose_name='Telefono')
    Direction = models.CharField(max_length=50, verbose_name='Direccion')
    gender = models.CharField(max_length=1, verbose_name='Genero')
    Eps = models.CharField(max_length=50, verbose_name='Eps')
    email = models.EmailField(max_length=100, verbose_name='Correo')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Fecha de cumpleaños')

    def __str__(self):
        return self.identification_number
