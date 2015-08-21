# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0004_auto_20150805_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlsite',
            name='submit_date',
        ),
    ]
