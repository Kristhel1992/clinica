from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Documento
from citas.models import Cita
from .forms import SubirDocumentoForm

def lista_documentos(request):
    documentos = Documento.objects.all()
    return render(request, 'documentos/lista.html', {'documentos': documentos})

@login_required
def subir_documento(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)
    
    # Verificar que el paciente es el dueño de la cita
    if request.user.tipo == 'paciente' and cita.paciente != request.user:
        messages.error(request, "No tienes permiso para subir documentos a esta cita")
        return redirect('mis_citas')
    
    if request.method == 'POST':
        form = SubirDocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            documento = form.save(commit=False)
            documento.cita = cita
            documento.save()
            messages.success(request, "¡Documento subido exitosamente!")
            return redirect('mis_citas')
    else:
        form = SubirDocumentoForm()
    
    return render(request, 'documentos/subir_documento.html', {'form': form, 'cita': cita})

@login_required
def mis_documentos(request):
    if request.user.tipo == 'paciente':
        citas = Cita.objects.filter(paciente=request.user)
        documentos = Documento.objects.filter(cita__in=citas).order_by('-fecha_subida')
    elif request.user.tipo == 'doctor':
        doctor = request.user.doctor
        citas = Cita.objects.filter(doctor=doctor)
        documentos = Documento.objects.filter(cita__in=citas).order_by('-fecha_subida')
    else:
        documentos = Documento.objects.all()
    
    return render(request, 'documentos/mis_documentos.html', {'documentos': documentos})
