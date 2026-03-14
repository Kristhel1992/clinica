from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    TIPO = (
        ('paciente', 'Paciente'),
        ('doctor', 'Doctor'),
    )
    tipo = models.CharField(max_length=20, choices=TIPO)
    telefono = models.CharField(max_length=20, unique=True, null=True, blank=True)

    def __str__(self):
        return self.username