# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-12 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0011_auto_20181112_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='picture',
            field=models.ImageField(upload_to=b'', verbose_name='Affiche du film'),
        ),
    ]
