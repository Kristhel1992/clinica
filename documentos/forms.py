from django import forms
from .models import Documento

class SubirDocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['tipo', 'archivo']
        labels = {
            'tipo': 'Tipo de Documento',
            'archivo': 'Archivo'
        }
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'archivo': forms.FileInput(attrs={'class': 'form-control'}),
        }
