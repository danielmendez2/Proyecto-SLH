from django.db import models


class Doctors(models.Model):
    Photo = models.ImageField(upload_to='imagenes', verbose_name='Foto', null=True, blank=True)
    Name = models.CharField(max_length=50, verbose_name='Nombre', blank=True, null=True)
    Surname = models.CharField(max_length=50, verbose_name='Apellido', blank=True, null=True)
    Cc = models.CharField(unique=True, max_length=11, null=True, blank=True, verbose_name='Cedula')
    Phone = models.CharField(max_length=13, verbose_name='Telefono', null=True,blank=True)
    Direction = models.CharField(max_length=50,verbose_name='direccion', null=True, blank=True)
    Gender = [
        ('M', 'MASCULINO'),
        ('F', 'FEMENINO'),
        ('O', 'OTRO')
    ]
    gender = models.CharField(max_length=1, verbose_name='Genero', choices=Gender)
    EPSS= [
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
    Eps = models.CharField(max_length=100, choices=EPSS, verbose_name='EPS', blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True, verbose_name='Coreeo electronico')
    Professional_card = models.CharField(max_length=30, unique=True, blank=True, null=True,
                                         verbose_name='Tarjeta profesional')
    specialization = [
        ('P', 'PEDIATRA'),
        ('D','DOCTOR GENERAL')
    ]
    Specialization = models.CharField(choices=specialization, max_length=100,
                                      verbose_name='Especializacion', null=True, blank=True)
    date_of_birth = models.DateField(verbose_name='Fecha de cumpleaños')
    meets_the_profile = models.BooleanField(verbose_name='Cumple oon el perfil')

    def __str__(self):
        return self.Name