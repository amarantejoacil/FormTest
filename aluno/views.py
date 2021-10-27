from django.shortcuts import render
from aluno.forms import AlunoForms


def AlunoView(request):
    form = AlunoForms()
    context = {'form':form}
    return render(request, 'aluno.html', context)


def Revisao_consulta(request):
    if request.method == 'POST':
        form = AlunoForms(request.POST)
        context = {'form': form}
        return render(request, 'minha_consulta.html', context)