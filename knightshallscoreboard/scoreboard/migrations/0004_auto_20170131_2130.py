# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-31 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0003_auto_20170131_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchinfo',
            name='numberRounds',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
