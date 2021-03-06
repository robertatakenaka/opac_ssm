# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 16:49
from __future__ import unicode_literals

import assets_manager.models
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=32, null=True)),
                ('file', models.FileField(max_length=500, upload_to=assets_manager.models.upload_to_path)),
                ('filename', models.CharField(blank=True, max_length=128, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Asset',
                'ordering': ['-created_at'],
                'verbose_name_plural': 'Assets',
            },
        ),
    ]
