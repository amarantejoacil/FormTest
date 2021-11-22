from django.contrib import admin
from .models import Medico, Paciente, Disciplina, Estudante, Matricula, Especialidade, Atendimento
# Register your models here.



admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Disciplina)
admin.site.register(Estudante)
admin.site.register(Matricula)
admin.site.register(Especialidade)
admin.site.register(Atendimento)