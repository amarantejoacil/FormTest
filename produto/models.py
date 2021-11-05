from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Produto(models.Model):
    descricao = models.CharField('Descrição', max_length=100)
    valor = models.DecimalField('Valor', max_digits=8, decimal_places=2)
    categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT)
    observacoes = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.descricao


class Categoria(models.Model):
    categoria_desc = models.CharField('Categoria Descrição', max_length=100)

    def __str__(self):
        return self.categoria_desc