from django.db import models

# Create your models here.
from APP.Nurse.models import Nurses
from APP.Doctor.models import Doctors
from APP.Patient.models import Patients


class Quotes(models.Model):
    date_and_time = models.DateTimeField()
    doctors = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    eps = models.CharField(max_length=50)
    specialty = models.CharField(max_length=50)

    def __str__(self):
        return self.patient.Name