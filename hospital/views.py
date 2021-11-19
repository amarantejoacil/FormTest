from django.shortcuts import render, redirect
from hospital.forms import MedicoModelForm
from .models import Medico
from django.http import JsonResponse
from rest_framework import viewsets
from hospital.serializer import MedicoSerializer
# Create your views here.


class MedicoViewSet(viewsets.ModelViewSet):
    """ exibindo todos os médicos cadastrados """
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer


def ConsultaView(request):
    obj_medico = Medico.objects.all()
    return render(request, 'consulta.html', {'obj_medico': obj_medico})


def CadastrarMedico(request):
    form = MedicoModelForm()
    if request.method == 'POST':
        form = MedicoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista-paciente')

    context = {
        'form': form
    }
    return render(request, 'cadastro_medico.html', context)


def AtualizaMedico(request, pk):
    medico = Medico.objects.get(id=pk)
    form = MedicoModelForm(instance=medico)

    if request.method == 'POST':
        form = MedicoModelForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect('lista-paciente')

    context = {
        'form': form
    }

    return render(request, 'cadastro_medico.html', context)


def DeletarMedico(request, pk):
    medico = Medico.objects.get(id=pk)
    if request.method == 'POST':
        medico.delete()
        return redirect('lista-paciente')

    context = {'medico':medico}
    return render(request, 'delete.html', context)




