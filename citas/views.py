from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cita
from .forms import AgendarCitaForm

def lista_citas(request):
    citas = Cita.objects.all()
    return render(request, 'citas/lista.html', {'citas': citas})

@login_required
def agendar_cita(request):
    if request.user.tipo != 'paciente':
        messages.error(request, "Solo los pacientes pueden agendar citas")
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = AgendarCitaForm(request.POST)
        if form.is_valid():
            cita = form.save(commit=False)
            cita.paciente = request.user
            cita.save()
            messages.success(request, "¡Cita agendada exitosamente!")
            return redirect('mis_citas')
    else:
        form = AgendarCitaForm()
    
    return render(request, 'citas/agendar_cita.html', {'form': form})

@login_required
def mis_citas(request):
    if request.user.tipo == 'paciente':
        citas = Cita.objects.filter(paciente=request.user).order_by('-fecha', '-hora')
    elif request.user.tipo == 'doctor':
        doctor = request.user.doctor
        citas = Cita.objects.filter(doctor=doctor).order_by('-fecha', '-hora')
    else:
        citas = Cita.objects.all()
    
    return render(request, 'citas/mis_citas.html', {'citas': citas})

