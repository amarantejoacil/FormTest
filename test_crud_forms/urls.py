"""test_crud_forms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from hospital.views import MedicoViewSet, PacienteViewSet, EstudanteViewSet, MatriculaViewSet, \
    DisciplinaViewSet, ListaPaciente, ListaMatriculaEstudante


router = routers.DefaultRouter()
router.register('medicos', MedicoViewSet, basename='medicos')
router.register('pacientes', PacienteViewSet, basename='pacientes')
router.register('estudantes', EstudanteViewSet, basename='estudantes')
router.register('disciplinas', DisciplinaViewSet, basename='disciplinas')
router.register('matriculas', MatriculaViewSet, basename='matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('produto.urls')),
    path('aluno/', include('aluno.urls')),
    path('medico/', include('hospital.urls')),
    path('api/', include(router.urls)),
    path('estudantes/<int:pk>/matriculas/', ListaMatriculaEstudante.as_view()),
]
