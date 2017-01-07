# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0006_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='imagen',
            field=models.ImageField(upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='document/%Y/%m/%d'),
        ),
    ]