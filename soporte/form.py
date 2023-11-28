from django import forms
from .models import Soporte

class SoporteForm(forms.ModelForm):
    class Meta:
        model = Soporte
        fields = '__all__'


        



