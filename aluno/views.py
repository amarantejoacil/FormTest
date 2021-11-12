from django.shortcuts import render
from aluno.forms import AlunoForms, PessoaForm
from .models import Pessoa


def AlunoView(request):
    aluno_form = AlunoForms()
    pessoa_form = PessoaForm()
    context = {'aluno_form':aluno_form, 'pessoa_form':pessoa_form}
    return render(request, 'aluno.html', context)


def Revisao_consulta(request):
    if request.method == 'POST':
        aluno_form = AlunoForms(request.POST)
        pessoa_form = PessoaForm(request.POST)
        if aluno_form.is_valid():
            context = {'aluno_form': aluno_form, 'pessoa_form': pessoa_form}
            # context = {'pessoa_form': pessoa_form}
            # cd = pessoa_form.cleaned_data
            #
            # pc = Pessoa(
            #     cpf=cd['cpf'],
            # )
            #
            # pc.save()
            return render(request, 'minha_consulta.html', context)
        else:
            context = {'aluno_form': aluno_form, 'pessoa_form': pessoa_form}
            # context = {'pessoa_form': pessoa_form}
            return render(request, 'aluno.html', context)




