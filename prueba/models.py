from django.db import models

# Create your models here.

class Persona(models.Model):
    nombres = models.CharField(max_length=100, null=False, blank=False)
    apellidos = models.CharField(max_length=100, null=False, blank=False)
    correo = models.EmailField(unique= True)

    class Meta:
        db_table = "personas"

