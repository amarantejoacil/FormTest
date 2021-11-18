from django.shortcuts import render
from hospital.forms import MedicoModelForm
from hospital.validation import *
# Create your views here.


def ConsultaView(request):
    return render(request, 'consulta.html')


def CadastrarMedico(request):
    if request.method == 'GET':
        form = MedicoModelForm()
        context = {
            'form': form
        }
        return render(request, 'cadastro_medico.html', context)
    else:
        #POST
        form = MedicoModelForm(request.POST)
        if form.is_valid():
            lista_erros = {}
            nome = form.data['nome']
            verifica_num_text(nome, 'nome', lista_erros)

            existe_erro = 'N'
            for e in lista_erros:
                mensagem_erro = lista_erros[e]
                form.add_error(e, mensagem_erro)
                existe_erro = 'S'


            if existe_erro == 'N':
                form.save()
                form = MedicoModelForm()  # limpo formulário
                context = {
                    'form': form
                }
                return render(request, 'consulta.html', context)
            else:
                context = {
                    'form': form
                }
                return render(request, 'cadastro_medico.html', context)






