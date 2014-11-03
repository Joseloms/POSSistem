# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0002_auto_20141028_1306'),
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='M2MModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('emplado', models.ForeignKey(to='empleados.Empleado')),
                ('equipos', models.ForeignKey(to='equipos.Equipo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='m2mmodel',
            unique_together=set([('emplado', 'equipos')]),
        ),
    ]
