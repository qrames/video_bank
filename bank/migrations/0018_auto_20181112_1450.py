# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-12 14:50
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0017_auto_20181112_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movietranslation',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True),
        ),
    ]
