# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('usertype', models.CharField(choices=[('Student', 'Student'), ('Tutor', 'Tutor')], max_length=8)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('firstname', models.CharField(blank=True, max_length=50)),
                ('lastname', models.CharField(blank=True, max_length=50)),
                ('mobile', models.CharField(blank=True, max_length=10, verbose_name='Mobile')),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.IntegerField(blank=True, default=0, null=True)),
                ('profilepicture', models.ImageField(blank=True, max_length=5000, null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
