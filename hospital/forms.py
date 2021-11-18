from django import forms
from .models import Medico


class MedicoModelForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['numero_registro', 'nome', 'data_nascimento']


    # numero_registro = forms.IntegerField(label='N° Registro')
    # nome = forms.CharField(label='Nome', max_length=100)
    # data_nascimento = forms.DateField(label='Data de nascimento')
    #
    # def clean(self):
    #     nome = self.cleaned_data.get('nome')
    #     if any(char.isdigit() for char in nome):
    #         raise forms.ValidationError('Não é permitido número neste campo!')
    #     else:
    #         return nome



    #