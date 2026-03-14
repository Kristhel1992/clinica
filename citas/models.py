from django.db import models
from usuarios.models import Usuario
from doctores.models import Doctor

class Cita(models.Model):

    ESTADO = (
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('atendida', 'Atendida'),
        ('cancelada', 'Cancelada'),
    )

    paciente = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        limit_choices_to={'tipo': 'paciente'}
    )

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADO, default='pendiente')

    class Meta:
        unique_together = ('doctor', 'fecha', 'hora')

    def __str__(self):
        return f"{self.paciente} - {self.fecha} {self.hora}"