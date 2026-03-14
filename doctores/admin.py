from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'especialidad')
    list_filter = ('especialidad',)
    search_fields = ('usuario__username', 'usuario__first_name', 'usuario__last_name')
