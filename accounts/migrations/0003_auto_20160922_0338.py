# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-22 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20160920_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='sexM',
        ),
        migrations.AlterField(
            model_name='profile',
            name='sexH',
            field=models.BooleanField(choices=[(True, 'Man'), (False, 'Woman')], default=True),
        ),
    ]
