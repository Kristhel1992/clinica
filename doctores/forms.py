from django import forms
from django.contrib.auth.forms import UserCreationForm
from usuarios.models import Usuario
from .models import Doctor

class RegistroDoctorForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True, label="Nombre")
    last_name = forms.CharField(max_length=150, required=True, label="Apellido")
    telefono = forms.CharField(max_length=20, required=False, label="Teléfono")
    especialidad = forms.ChoiceField(choices=Doctor.ESPECIALIDAD, label="Especialidad")

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'first_name', 'last_name', 'telefono', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.tipo = 'doctor'
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar Contraseña"
        self.fields['username'].label = "Usuario"
