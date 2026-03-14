from django.contrib import admin
from .models import Documento

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'cita', 'fecha_subida', 'revisado')
    list_filter = ('tipo', 'revisado')
    search_fields = ('cita__paciente__username', 'tipo')
    date_hierarchy = 'fecha_subida'
    readonly_fields = ('fecha_subida',)
