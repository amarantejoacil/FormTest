from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.AlunoView, name='lista-aluno'),
    path('minha_consulta/', views.Revisao_consulta, name='minha-consulta'),
]