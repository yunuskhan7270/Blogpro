# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-08-12 18:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_data',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='blog_data',
            name='like',
        ),
    ]