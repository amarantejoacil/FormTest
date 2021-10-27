from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Produto
from django.urls import reverse_lazy

#LISTANDO
class IndexView(ListView):
    model = Produto
    template_name = 'index.html'


#CREATE
class CreateProduto(CreateView):
    model = Produto
    fields = ['descricao', 'valor', 'categoria']
    template_name = 'modelo_formulario.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['botao'] = 'Cadastrar Registro'
        return context


#UPDATE
class UpdateProduto(UpdateView):
    model = Produto
    fields = ['descricao', 'valor', 'categoria']
    template_name = 'modelo_formulario.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['botao'] = 'Atualizar Registro'
        return context


#DELETE
class DeleteProduto(DeleteView):
    model = Produto
    template_name = 'modelo_formulario_excluir.html'
    success_url = reverse_lazy('index')


