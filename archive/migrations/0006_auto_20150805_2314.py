# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0005_remove_urlsite_submit_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='urlSite',
            new_name='urlSites',
        ),
    ]
