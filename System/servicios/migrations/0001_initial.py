# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0002_auto_20141029_0855'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_cracion', models.DateTimeField(auto_now_add=True)),
                ('fecha_a_agendar', models.DateTimeField()),
                ('descripcion', models.TextField(blank=True)),
                ('observaciones', models.TextField(blank=True)),
                ('fecha_terminacion', models.DateTimeField(auto_now=True)),
                ('empleado', models.ForeignKey(to='empleados.Empleado', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tipo_Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='servicio',
            name='tipo',
            field=models.ForeignKey(to='servicios.Tipo_Servicio', blank=True),
            preserve_default=True,
        ),
    ]
