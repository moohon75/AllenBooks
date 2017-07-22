# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-22 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=0, max_digits=10)),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateField()),
            ],
        ),
    ]
