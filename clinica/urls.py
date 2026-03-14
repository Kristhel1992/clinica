"""
URL configuration for clinica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from usuarios.views import registro_paciente, dashboard_paciente
from doctores.views import registro_doctor, dashboard_doctor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    
    path('registro/paciente/', registro_paciente, name='registro_paciente'),
    path('registro/doctor/', registro_doctor, name='registro_doctor'),
    
    path('dashboard-paciente/', dashboard_paciente, name='dashboard_paciente'),
    path('dashboard-doctor/', dashboard_doctor, name='dashboard_doctor'),

    path('usuarios/', include('usuarios.urls')),
    path('doctores/', include('doctores.urls')),
    path('citas/', include('citas.urls')),
    path('documentos/', include('documentos.urls')),
    path('chatbot/', include('chatbot.urls')),
]