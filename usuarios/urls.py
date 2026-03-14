from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_usuarios, name='lista_usuarios'),
    path('registro/', views.registro_paciente, name='registro_paciente'),
    path('dashboard/', views.dashboard_paciente, name='dashboard_paciente'),
]