# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-12 15:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_bigc_image_preview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bigc',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='bigc',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='bigc',
            name='text',
        ),
    ]