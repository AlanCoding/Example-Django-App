# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

from rockband.migrations._create_delete_scripts import make_bands, delete_all


class Migration(migrations.Migration):

    dependencies = [
        ('rockband', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(make_bands, delete_all),
    ]
