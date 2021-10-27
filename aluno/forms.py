from django import forms


class AlunoForms(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    data_nascimento = forms.DateTimeField(label='Data de nascimento')



