# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 07:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0008_auto_20170417_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subjectid', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='categories',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor.Subject'),
        ),
    ]
