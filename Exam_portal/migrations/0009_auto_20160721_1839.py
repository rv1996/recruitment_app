# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-21 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exam_portal', '0008_reviewflag'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ReviewFlag',
        ),
        migrations.AlterField(
            model_name='student',
            name='skills',
            field=models.CharField(max_length=2255),
        ),
    ]
