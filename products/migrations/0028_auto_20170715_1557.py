# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-15 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_auto_20170713_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officesupply',
            name='SNR_Available',
            field=models.CharField(default=' ', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='officesupply',
            name='SNR_Brand',
            field=models.CharField(default=' ', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='officesupply',
            name='SNR_Description',
            field=models.CharField(default=' ', max_length=8000, null=True),
        ),
        migrations.AlterField(
            model_name='officesupply',
            name='SNR_ImageURL',
            field=models.CharField(default=' ', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='officesupply',
            name='SNR_ModelNo',
            field=models.CharField(default=' ', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='officesupply',
            name='SNR_Price',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=50),
        ),
        migrations.AlterField(
            model_name='officesupply',
            name='SNR_ProductURL',
            field=models.CharField(default=' ', max_length=2000),
        ),
        migrations.AlterField(
            model_name='officesupply',
            name='SNR_Title',
            field=models.CharField(default=' ', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='officesupply',
            name='SNR_UPC',
            field=models.CharField(default=' ', max_length=500, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='officesupply',
            unique_together=set([('SNR_SKU', 'SNR_ProductURL', 'SNR_Price')]),
        ),
    ]