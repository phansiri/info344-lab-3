# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('archive', '0007_urlsites_screenshot'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlsites',
            name='owner',
            field=models.ForeignKey(related_name='archive', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
