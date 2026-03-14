from django.contrib import admin
from .models import Cita

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'doctor', 'fecha', 'hora', 'estado')
    list_filter = ('estado', 'fecha')
    search_fields = ('paciente__username', 'doctor__usuario__username')
    date_hierarchy = 'fecha'
