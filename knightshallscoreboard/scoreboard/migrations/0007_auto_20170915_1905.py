# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-15 19:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0006_auto_20170324_0129'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teaminfo',
            options={'ordering': ['teamName']},
        ),
    ]
