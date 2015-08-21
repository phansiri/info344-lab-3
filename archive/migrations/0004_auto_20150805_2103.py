# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0003_auto_20150805_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlsite',
            name='finalUrl',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='urlsite',
            name='httpStatusCode',
            field=models.CharField(max_length=5, blank=True),
        ),
        migrations.AlterField(
            model_name='urlsite',
            name='pageTitle',
            field=models.CharField(max_length=400, blank=True),
        ),
    ]
