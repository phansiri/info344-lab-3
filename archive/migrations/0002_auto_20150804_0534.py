# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('archive', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='urlSite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('originalUrl', models.CharField(max_length=1000)),
                ('finalUrl', models.CharField(max_length=1000)),
                ('httpStatusCode', models.CharField(max_length=5)),
                ('pageTitle', models.CharField(max_length=400)),
                ('submit_date', models.DateTimeField(null=True, blank=True)),
                ('submitter', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='url',
        ),
    ]
