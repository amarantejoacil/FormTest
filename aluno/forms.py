from django import forms


class AlunoForms(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    idade = forms.IntegerField(label='Idade')


