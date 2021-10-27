from django import forms
from tempus_dominus.widgets import DatePicker


class AlunoForms(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    data_nascimento = forms.DateTimeField(label='Data de nascimento', widget=DatePicker())



