# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 08:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170523_1312'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bibliouser',
            options={'permissions': (('can_rent', 'Can rent a book'),)},
        ),
    ]
