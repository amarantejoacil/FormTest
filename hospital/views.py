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
        form = MedicoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'consulta.html')
        else:
            context = {
                'form': form
            }
            return render(request, 'cadastro_medico.html', context)
