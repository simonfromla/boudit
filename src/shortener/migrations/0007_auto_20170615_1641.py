# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-15 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0006_shawtyurl_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shawtyurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
