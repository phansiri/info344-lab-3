# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0002_auto_20150804_0534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlsite',
            name='submitter',
        ),
        migrations.AlterField(
            model_name='urlsite',
            name='finalUrl',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='urlsite',
            name='originalUrl',
            field=models.URLField(),
        ),
    ]
