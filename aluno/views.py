from django.shortcuts import render
from aluno.forms import AlunoForms


def AlunoView(request):
    form = AlunoForms()
    context = {'form':form}
    return render(request, 'aluno.html', context)