from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.ConsultaView, name='lista-paciente'),
    path('cadastrar/', views.CadastrarMedico, name='cadastrar-medico'),
    path('atualizar/', views.CadastrarMedico, name='cadastrar-medico'),
]
