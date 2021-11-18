from django.shortcuts import render
from hospital.forms import MedicoModelForm
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
            obj_medico = form.save()
            form = MedicoModelForm() #limpo formulário



        #retorno do contexto executa independente do formulario ser valido
        context = {
            'form': form
        }
        return render(request, 'consulta.html', context)




