# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('time', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
            ],
        ),
    ]
