# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sensorid', models.CharField(default=b'', max_length=100)),
                ('valType', models.CharField(default=b'', max_length=100)),
                ('data', models.TextField()),
            ],
        ),
    ]
