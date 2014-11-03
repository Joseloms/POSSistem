# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0002_auto_20141029_0855'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='M2MModel',
            new_name='Empleado2Equipos',
        ),
    ]
