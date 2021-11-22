from django.shortcuts import render, redirect
from hospital.forms import MedicoModelForm
from .models import Medico, Paciente, Disciplina, Estudante, Matricula, Atendimento
from django.http import JsonResponse
from rest_framework import viewsets, generics
from hospital.serializer import MedicoSerializer, PacienteSerializer, ListaPacientePorMedicoSerializer, \
    MatriculaSerializer, EstudanteSerializer, DisciplinaSerializer, ListaMatriculasEstudanteSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class MedicoViewSet(viewsets.ModelViewSet):
    """ exibindo todos os médicos cadastrados """
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer


class PacienteViewSet(viewsets.ModelViewSet):
    """ exibindo todos os Pacientes e médico vinculado """
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    # para acessa será necessário autenticação
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaPaciente(generics.ListAPIView):
    """Listando todos pacientes de determinado médico"""
    def get_queryset(self):
        queryset = Paciente.objects.filter(medico_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaPacientePorMedicoSerializer


class ListaMatriculaEstudante(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer


class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


def ConsultaView(request):
    obj_medico = Medico.objects.all()
    # obj_atendimento = Atendimento.objects.all()
    return render(request, 'consulta.html', {'obj_medico': obj_medico})


def CadastrarMedico(request):
    form = MedicoModelForm()
    if request.method == 'POST':
        form = MedicoModelForm(request.POST)
        if form.is_valid():
            form.save()
            # form.save_m2m()
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
            # form.save_m2m()
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




