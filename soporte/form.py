from django import forms
from .models import Soporte, Cliente


class SoporteForm(forms.ModelForm):
    class Meta:
        model = Soporte
        fields = ['nombre_pc', 'descripcion_pc', 'descripcion_problema', 'prioridad', 'estado', 'fecha', 'cliente']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'documento', 'direccion', 'correo']

        



