# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-21 10:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clickevent',
            old_name='kirr_url',
            new_name='shawty_url',
        ),
    ]