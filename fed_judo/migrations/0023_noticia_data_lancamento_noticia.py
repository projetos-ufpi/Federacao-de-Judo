# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-22 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fed_judo', '0022_noticia'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='data_lancamento_noticia',
            field=models.DateTimeField(null=True),
        ),
    ]
