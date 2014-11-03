# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20141031_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unidades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='producto',
            name='peso',
            field=models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='producto',
            name='sku',
            field=models.CharField(max_length=140, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='producto',
            name='slug',
            field=models.SlugField(null=True, blank=True, help_text=b'Valor unico por producto URL pagina, creado desde nombre.', unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='producto',
            name='unidad',
            field=models.ForeignKey(default=2, blank=True, to='productos.Unidades'),
            preserve_default=False,
        ),
    ]
