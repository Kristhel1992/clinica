from django.db import models
from citas.models import Cita

class Documento(models.Model):
    TIPO = (
        ('radiografia', 'Radiografía'),
        ('analisis', 'Análisis Clínico'),
    )

    cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=30, choices=TIPO)
    archivo = models.FileField(upload_to='documentos/')
    fecha_subida = models.DateTimeField(auto_now_add=True)
    revisado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.tipo} - {self.cita.__str__()}"