from django.db import models
from usuarios.models import Usuario

class Doctor(models.Model):

    ESPECIALIDAD = (
        ('odontologo', 'Odontólogo'),
        ('medico_general', 'Médico General'),
    )

    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=30, choices=ESPECIALIDAD)

    def __str__(self):
        return f"{self.usuario.username} - {self.especialidad}"