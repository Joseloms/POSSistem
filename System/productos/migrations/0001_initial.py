# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marcas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
                ('imagen', models.ImageField(upload_to=b'images/producto', null=True, verbose_name=b'Logo Marca', blank=True)),
                ('presenatacion', models.CharField(max_length=140)),
                ('precio', models.DecimalField(max_digits=9, decimal_places=2)),
                ('marca', models.ForeignKey(to='marcas.Marca', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
