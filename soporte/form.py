from django import forms
from .models import Soporte, Cliente


class SoporteForm(forms.ModelForm):
    class Meta:
        model = Soporte
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'documento', 'direccion', 'correo']

        



