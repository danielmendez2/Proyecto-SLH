from django.db import models
from APP.Person.models import People


class Doctors(models.Model):
    name = models.ForeignKey(People, on_delete=models.CASCADE)
    professional_card = models.CharField(max_length=30)
    specialization = models.CharField(max_length=50)

    def __str__(self):
        return self.name.Name