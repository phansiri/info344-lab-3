# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('originalUrl', models.CharField(max_length=1000)),
                ('finalUrl', models.CharField(max_length=1000)),
                ('httpStatusCode', models.CharField(max_length=5)),
                ('pageTitle', models.CharField(max_length=400)),
            ],
        ),
    ]
