from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Usuario
from .forms import RegistroPacienteForm
from citas.models import Cita

def lista_usuarios(request):
    usuarios = Usuario.objects.filter(tipo='paciente')
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})

def registro_paciente(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = RegistroPacienteForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "¡Registro exitoso! Ahora puedes iniciar sesión.")
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = RegistroPacienteForm()
    
    return render(request, 'usuarios/registro_paciente.html', {'form': form})

@login_required(login_url='login')
def dashboard_paciente(request):
    if request.user.tipo != 'paciente':
        return redirect('dashboard')
    
    # Obtener próximas citas del paciente
    proximas_citas = Cita.objects.filter(
        paciente=request.user,
        fecha__gte=timezone.now().date()
    ).order_by('fecha', 'hora')[:5]
    
    context = {
        'proximas_citas': proximas_citas,
    }
    
    return render(request, 'dashboard_paciente.html', context)