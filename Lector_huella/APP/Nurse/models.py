from django.db import models

# Create your models here.
from django.core.exceptions import ValidationError
from APP.Person.models import People


class Nurses(models.Model):
    data = models.ForeignKey(People, on_delete=models.CASCADE)
    Professional_card = models.CharField(max_length=30,unique=True)
    Specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.data.Name
    class Meta:
        verbose_name = 'Nurse'
