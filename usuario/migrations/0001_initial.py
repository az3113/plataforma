# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 06:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(blank=True, max_length=40)),
                ('key_expires', models.DateTimeField(default=datetime.date.today)),
                ('activacion_url', models.CharField(max_length=5, null=True)),
            ],
            options={
                'verbose_name_plural': 'Perfiles de Usuario',
            },
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('dni', models.CharField(max_length=8)),
                ('gender', models.CharField(choices=[('s', ' student'), ('t', 'teacher')], default='s', max_length=128)),
                ('acceso_free', models.DateTimeField(auto_now_add=True)),
                ('acceso', models.CharField(default=False, max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario'),
        ),
    ]
