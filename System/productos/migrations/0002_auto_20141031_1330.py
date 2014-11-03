# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to=b'images/producto', null=True, verbose_name=b'Imagen Producto', blank=True),
            preserve_default=True,
        ),
    ]
