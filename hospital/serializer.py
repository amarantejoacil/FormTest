from rest_framework import serializers
from hospital.models import Medico


class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['id', 'numero_registro', 'nome']
