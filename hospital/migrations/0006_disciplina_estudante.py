# Generated by Django 3.2.8 on 2021-11-19 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_alter_medico_data_nascimento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Estudante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome Estudante')),
            ],
        ),
    ]
