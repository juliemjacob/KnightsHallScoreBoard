# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-31 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchtype',
            name='maxRounds',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='matchtype',
            name='maxScore',
            field=models.IntegerField(null=True),
        ),
    ]
