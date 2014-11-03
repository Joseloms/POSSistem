# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipo',
            old_name='seial',
            new_name='serial',
        ),
    ]
