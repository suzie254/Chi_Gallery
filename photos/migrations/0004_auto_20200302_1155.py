# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-03-02 08:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20200301_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='photos.category'),
        ),
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/'),
        ),
    ]
