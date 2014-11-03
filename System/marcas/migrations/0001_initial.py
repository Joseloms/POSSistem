# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
                ('logo', models.ImageField(upload_to=b'images/', null=True, verbose_name=b'Logo Marca', blank=True)),
                ('empresa', models.ForeignKey(to='empresas.Empresa', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
