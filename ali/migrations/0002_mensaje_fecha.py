# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-30 18:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ali', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='fecha',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]