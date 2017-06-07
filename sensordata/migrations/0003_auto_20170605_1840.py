# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensordata', '0002_auto_20170605_1816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor',
            old_name='data',
            new_name='senseVal',
        ),
    ]
