from django import forms
from tempus_dominus.widgets import DatePicker, DateTimePicker, TimePicker
from datetime import datetime
from aluno.validation import *


class AlunoForms(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    senha = forms.CharField(label='Senha', max_length=100)
    repete_senha = forms.CharField(label='Repete Senha', max_length=100)
    data_nascimento = forms.DateField(label='Data de nascimento', widget=DatePicker(), required=False)
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True,
                                    initial=datetime.today(), required=False)

    origem = forms.CharField(label='origem', max_length=100, required=False)
    destino = forms.CharField(label='destino', max_length=100, required=False)






    TIPO = {
        (1, 'Masculino'),
        (2, 'Feminino'),
        (3, 'Prefiro não informar')
    }

    sexo = forms.ChoiceField(label='Tipo de classe', choices=TIPO)
    bio = forms.CharField(
        label='Escreva sobre você',
        max_length=200,
        widget=forms.Textarea(),
        required=False
    )
    email = forms.EmailField(label='E-mail', max_length=150, required=False)

    data_hora = forms.DateTimeField(
        required=False,
        widget=DateTimePicker(
            options={
                'useCurrent': True,
                'collapse': False,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            }
        ),
    )

    horas = forms.TimeField(
        required=False,
        widget=TimePicker(
            options={
                'enabledHours': [9, 10, 11, 12, 13, 14, 15, 16],
                'defaultDate': '1970-01-01T14:56:00'
            },
            attrs={
                'input_toggle': True,
                'input_group': False,
            },
        ),
    )

    data_intervalo = forms.DateField(
        required=False,
        widget=DatePicker(
            options={
                'minDate': '2009-01-20',
                'maxDate': '2017-01-20',
            },
        ),
        initial='2013-01-01',
    )

    #VALIDAÇÃO MODELO 01
    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if any(char.isdigit() for char in nome):
            raise forms.ValidationError('Não é permitido números neste campo!')
        else:
            return nome

    def clean(self):
        # origem = self.cleaned_data.get('origem')
        # destino = self.cleaned_data.get('destino')

        # VALIDAÇÃO MODELO 02
        # if origem == destino:
        #     self.add_error('destino', 'Origem e Destino não podem ser iguais')
        # return self.cleaned_data


        # VALIDAÇÃO MODELO 03
        lista_de_erros = {}
        senha = self.cleaned_data.get('senha')
        repete_senha = self.cleaned_data.get('repete_senha')

        verifica_numero_existe_em_texto(senha, 'senha', lista_de_erros)
        verifica_numero_existe_em_texto(repete_senha, 'repete_senha', lista_de_erros)
        verificar_senha_iguais(senha, repete_senha, lista_de_erros)

        #verifica se existe erro
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)


        return self.cleaned_data











