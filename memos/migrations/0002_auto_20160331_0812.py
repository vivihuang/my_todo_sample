# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memo',
            name='status',
        ),
        migrations.AddField(
            model_name='memo',
            name='active_status',
            field=models.BooleanField(default=True),
        ),
    ]