# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-20 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credential', '0003_auto_20170720_0624'),
    ]

    operations = [
        migrations.CreateModel(
            name='sendFriends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]