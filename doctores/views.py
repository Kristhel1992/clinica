from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Doctor
from .forms import RegistroDoctorForm
from citas.models import Cita
from documentos.models import Documento
from usuarios.models import Usuario

def lista_doctores(request):
    doctores = Doctor.objects.all()
    return render(request, 'doctores/lista.html', {'doctores': doctores})

def registro_doctor(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = RegistroDoctorForm(request.POST)
        if form.is_valid():
            user = form.save()
            especialidad = form.cleaned_data['especialidad']
            doctor = Doctor.objects.create(usuario=user, especialidad=especialidad)
            messages.success(request, "¡Registro exitoso! Ahora puedes iniciar sesión.")
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = RegistroDoctorForm()
    
    return render(request, 'doctores/registro_doctor.html', {'form': form})

@login_required(login_url='login')
def dashboard_doctor(request):
    if request.user.tipo != 'doctor':
        return redirect('dashboard')
    
    try:
        doctor = Doctor.objects.get(usuario=request.user)
        
        # Obtener citas del doctor
        citas = Cita.objects.filter(doctor=doctor).order_by('-fecha')
        
        # Obtener pacientes únicos del doctor
        pacientes = Usuario.objects.filter(
            tipo='paciente',
            cita__doctor=doctor
        ).distinct()
        
        # Obtener documentos de las citas del doctor
        documentos = Documento.objects.filter(
            cita__doctor=doctor
        ).order_by('-fecha_subida')
        
        context = {
            'doctor': doctor,
            'citas': citas,
            'pacientes': pacientes,
            'documentos': documentos,
            'citas_pendientes': citas.filter(estado='pendiente').count(),
            'total_documentos_nuevos': documentos.filter(revisado=False).count(),
        }
        return render(request, 'doctores/dashboard_doctor.html', context)
    except Doctor.DoesNotExist:
        messages.error(request, "No estás registrado como doctor")
        return redirect('dashboard')