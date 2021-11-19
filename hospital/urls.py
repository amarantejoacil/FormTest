from django.urls import path
from . import views




urlpatterns = [
    path('listar/', views.ConsultaView, name='lista-paciente'),
    path('cadastrar/', views.CadastrarMedico, name='cadastrar-medico'),
    path('atualizar/<int:pk>/', views.AtualizaMedico, name='atualizar-medico'),
    path('deletar/<int:pk>/', views.DeletarMedico, name='deletar-medico'),
]