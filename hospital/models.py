from django.db import models

# Create your models here.



class Medico(models.Model):
    numero_registro = models.IntegerField('N° de Registro')
    nome = models.CharField('Nome', max_length=100)
    data_nascimento = models.DateField('Data de nascimento')

    def __str__(self):
        return self.nome


class Paciente(models.Model):
    medico = models.ForeignKey('Medico', on_delete=models.PROTECT)
    nome = models.CharField('Nome', max_length=100)
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    sexo = models.CharField('Sexo', choices=SEXO, max_length=1)

    def __str__(self):
        return 'Paciente: ' + self.nome + '| Medico: ' + str(self.medico)



