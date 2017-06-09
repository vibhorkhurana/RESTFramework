# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sensorid', models.CharField(default=b'', max_length=100)),
                ('valType', models.CharField(default=b'', max_length=100)),
                ('senseVal', models.TextField()),
                ('owner', models.ForeignKey(related_name='sensors', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
