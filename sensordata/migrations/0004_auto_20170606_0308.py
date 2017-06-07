# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensordata', '0003_auto_20170605_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='sensorid',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='valType',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
    ]
