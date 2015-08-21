# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0006_auto_20150805_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlsites',
            name='screenShot',
            field=models.URLField(blank=True),
        ),
    ]
