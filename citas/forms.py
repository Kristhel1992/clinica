from django import forms
from .models import Cita
from doctores.models import Doctor

class AgendarCitaForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.all(),
        label="Selecciona Doctor",
        empty_label="Elige un doctor"
    )
    
    class Meta:
        model = Cita
        fields = ['doctor', 'fecha', 'hora', 'motivo']
        labels = {
            'fecha': 'Fecha',
            'hora': 'Hora',
            'motivo': 'Motivo de la consulta'
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'motivo': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        especialidad = kwargs.pop('especialidad', None)
        super().__init__(*args, **kwargs)
        
        self.fields['doctor'].widget.attrs.update({'class': 'form-control'})
        
        if especialidad:
            self.fields['doctor'].queryset = Doctor.objects.filter(especialidad=especialidad)
