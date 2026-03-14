from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_citas, name='lista_citas'),
    path('agendar/', views.agendar_cita, name='agendar_cita'),
    path('mis-citas/', views.mis_citas, name='mis_citas'),
]