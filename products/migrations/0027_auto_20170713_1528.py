# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-13 15:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_auto_20170713_1512'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='movies',
            unique_together=set([('SNR_SKU', 'SNR_ProductURL', 'SNR_Price')]),
        ),
    ]
