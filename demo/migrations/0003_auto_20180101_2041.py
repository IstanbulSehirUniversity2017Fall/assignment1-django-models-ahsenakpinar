# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-01 17:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20171213_0024'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cat_type', models.CharField(choices=[('1', 'Electronic'), ('2', 'cosmetic'), ('3', 'Clothing'), ('4', 'Cleaning'), ('5', 'Car')], default='1', max_length=20)),
                ('is_favorite', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='phonebrand',
            name='type',
        ),
        migrations.AddField(
            model_name='phonebrand',
            name='is_favorite',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='phonemodel',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='phonebrand',
            name='cat_type',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='demo.CategoryModel'),
        ),
    ]