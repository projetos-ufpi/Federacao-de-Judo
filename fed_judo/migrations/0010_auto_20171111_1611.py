# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fed_judo', '0009_auto_20171111_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='idade',
            field=models.IntegerField(null=True),
        ),
    ]
