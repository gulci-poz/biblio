# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 03:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0002_auto_20170520_0445'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookcategory',
            options={'verbose_name_plural': 'book categories'},
        ),
    ]