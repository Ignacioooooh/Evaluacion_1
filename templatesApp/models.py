from django.db import models

# Create your models here.

class Persona(models.Model):
    id = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
    



