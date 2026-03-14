from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from usuarios.models import Usuario
from doctores.models import Doctor
from citas.models import Cita
from documentos.models import Documento
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def webhook_chat(request):
    if request.method == "POST":
        return JsonResponse({"mensaje": "Webhook recibido correctamente"})
    return JsonResponse({"mensaje": "Solo POST permitido"})
def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, 'login.html')

@login_required(login_url='login')
def dashboard(request):
    # Si es doctor, redirigir al panel de doctor
    if request.user.tipo == 'doctor':
        return redirect('dashboard_doctor')

    # Si es paciente, redirigir al panel de paciente
    if request.user.tipo == 'paciente':
        return redirect('dashboard_paciente')

    # Panel de administrador
    if request.user.is_staff or request.user.is_superuser:
        pacientes_count = Usuario.objects.filter(tipo='paciente').count()
        doctores_count = Doctor.objects.count()
        citas_count = Cita.objects.count()
        documentos_count = Documento.objects.count()

        context = {
            'pacientes_count': pacientes_count,
            'doctores_count': doctores_count,
            'citas_count': citas_count,
            'documentos_count': documentos_count,
        }
        return render(request, 'admin_dashboard.html', context)

    # Fallback a dashboard genérico
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('home')
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
