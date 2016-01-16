# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-12 23:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbeamd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitylog',
            name='comments',
            field=models.ManyToManyField(blank=True, to='cbeamd.ActivityLogComment'),
        ),
        migrations.AlterField(
            model_name='mission',
            name='assigned_to',
            field=models.ManyToManyField(blank=True, to='cbeamd.User'),
        ),
    ]
