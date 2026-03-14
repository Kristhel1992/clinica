from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_documentos, name='lista_documentos'),
    path('subir/<int:cita_id>/', views.subir_documento, name='subir_documento'),
    path('mis-documentos/', views.mis_documentos, name='mis_documentos'),
]
