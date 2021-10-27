from django.urls import path
from .views import IndexView, CreateProduto, UpdateProduto, DeleteProduto

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cadastrar', CreateProduto.as_view(), name='cadastrar'),
    path('alterar/<int:pk>', UpdateProduto.as_view(), name='alterar'),
    path('deletar/<int:pk>', DeleteProduto.as_view(), name='deletar'),

]