# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 11:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resenha', '0002_livro_isbn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacao',
            name='usuario',
        ),
    ]