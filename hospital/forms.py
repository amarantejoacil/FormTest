from django import forms
from .models import Medico
from hospital.validation import *


class MedicoModelForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['numero_registro', 'nome', 'data_nascimento']

    def clean(self):
        lista_erros = {}
        nome = self.cleaned_data.get('nome')
        verifica_num_text(nome, 'nome', lista_erros)

        # verifica se existe erro
        if lista_erros is not None:
            for erro in lista_erros:
                mensagem_erro = lista_erros[erro]
                self.add_error(erro, mensagem_erro)

        return self.cleaned_data




    #