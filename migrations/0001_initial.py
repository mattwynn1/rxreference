# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-25 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SplDrug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=700)),
                ('idcode', models.CharField(max_length=100)),
                ('packager', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
