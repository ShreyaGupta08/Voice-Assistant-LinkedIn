# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-12-30 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_profile',
            name='location',
            field=models.TextField(blank=True),
        ),
    ]
