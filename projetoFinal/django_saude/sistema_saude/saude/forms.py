from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):

    data_consulta = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    class Meta:
        model = Paciente
        fields = ['nome', 'idade', 'sintomas', 'prioridade', 'data_consulta']
