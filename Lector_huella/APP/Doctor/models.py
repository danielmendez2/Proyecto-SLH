from django.db import models
from APP.Person.models import persona


class medico(models.Model):
    nombre = models.ForeignKey(persona, on_delete=models.CASCADE)
    tarjeta_profesional = models.CharField(max_length=30)
    especializacion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre.Name