from django.db import models

# Create your models here.


class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=100)

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    cpf = models.CharField('CPF', max_length=100)
    data_nascimento = models.DateField('Data Nascimento', null=True, blank=True)

    def __str__(self):
        return self.cpf