# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-05 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0005_auto_20181105_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviegenre',
            name='label',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
    ]