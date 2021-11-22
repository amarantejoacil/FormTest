from django.db import models


class Atendimento (models.Model):
    descricao = models.CharField('descricao', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.descricao


class Especialidade(models.Model):
    descricao = models.CharField('descricao', max_length=100)

    def __str__(self):
        return self.descricao


class Medico(models.Model):
    numero_registro = models.IntegerField('N° de Registro')
    nome = models.CharField('Nome', max_length=100)
    data_nascimento = models.DateField('Data de nascimento', null=True, blank=True)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.PROTECT, null=True, blank=True)
    atendimento = models.ManyToManyField(Atendimento)

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


class Estudante(models.Model):
    nome = models.CharField('Nome Estudante', max_length=100)

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    descricao = models.CharField('Descrição', max_length=100)

    def __str__(self):
        return  self.descricao


class Matricula(models.Model):

    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
    )
    periodo = models.CharField('Periodo', choices=PERIODO, max_length=1)
    estudante = models.ForeignKey(Estudante, on_delete=models.PROTECT)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)


    def __str__(self):
        return 'Periodo: '+ self.periodo + ' - Aluno: ' + str(self.estudante) + ' Disciplina: '+ str(self.disciplina)

