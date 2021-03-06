# Generated by Django 3.2.8 on 2021-11-19 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_disciplina_estudante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(choices=[('M', 'Matutino'), ('V', 'Vespertino')], max_length=1, verbose_name='Periodo')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hospital.disciplina')),
                ('estudante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hospital.estudante')),
            ],
        ),
    ]
