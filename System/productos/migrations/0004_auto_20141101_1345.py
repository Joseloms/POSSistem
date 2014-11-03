# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20141031_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='es_activo',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='producto',
            name='promocion',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=1, blank=True),
            preserve_default=False,
        ),
    ]
