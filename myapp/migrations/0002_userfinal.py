# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-19 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userfinal',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.TextField(blank=True, null=True)),
                ('level', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('consumerid', models.TextField(blank=True, null=True)),
                ('created_at', models.TextField(blank=True, null=True)),
                ('perishable_token', models.TextField(blank=True, null=True)),
                ('session_token', models.TextField(blank=True, null=True)),
                ('regid', models.TextField(blank=True, null=True)),
                ('username', models.TextField(blank=True, null=True)),
                ('updated_at', models.TextField(blank=True, null=True)),
                ('column_12', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'userfinal',
                'managed': False,
            },
        ),
    ]
