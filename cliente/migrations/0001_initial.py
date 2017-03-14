# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('mail', models.EmailField(max_length=254)),
                ('direccrion', models.CharField(max_length=200)),
                ('telefono', models.IntegerField(max_length=20)),
                ('ordenesTrabajos', models.CharField(max_length=200)),
            ],
        ),
    ]
