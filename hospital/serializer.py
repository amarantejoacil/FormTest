from rest_framework import serializers
from hospital.models import Medico, Paciente, Disciplina, Estudante, Matricula


class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['id', 'numero_registro', 'nome']


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'


class ListaPacientePorMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['nome', 'numero_registro']


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'


class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = ['disciplina', 'periodo']