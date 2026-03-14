from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_doctores, name='lista_doctores'),
    path('registro/', views.registro_doctor, name='registro_doctor'),
    path('dashboard/', views.dashboard_doctor, name='dashboard_doctor'),
]