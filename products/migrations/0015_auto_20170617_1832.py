# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-17 18:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20170615_2321'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='toys',
            unique_together=set([('SNR_SKU', 'SNR_ModelNo')]),
        ),
    ]
