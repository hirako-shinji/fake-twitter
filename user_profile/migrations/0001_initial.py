# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-07 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_shinigami', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
    ]