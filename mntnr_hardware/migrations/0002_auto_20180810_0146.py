# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-10 01:46
from __future__ import unicode_literals

from django.db import migrations
import mountaineer.core.models
import mountaineer.core.utils.slug


class Migration(migrations.Migration):

    dependencies = [
        ('mntnr_hardware', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabinet',
            name='slug',
            field=mountaineer.core.models.SlugField(db_index=True, default=mountaineer.core.utils.slug.slugid_nice, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='cabinetassignment',
            name='slug',
            field=mountaineer.core.models.SlugField(db_index=True, default=mountaineer.core.utils.slug.slugid_nice, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='datacenter',
            name='slug',
            field=mountaineer.core.models.SlugField(db_index=True, default=mountaineer.core.utils.slug.slugid_nice, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='networkdevice',
            name='slug',
            field=mountaineer.core.models.SlugField(db_index=True, default=mountaineer.core.utils.slug.slugid_nice, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='portassignment',
            name='slug',
            field=mountaineer.core.models.SlugField(db_index=True, default=mountaineer.core.utils.slug.slugid_nice, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='powerdistributionunit',
            name='slug',
            field=mountaineer.core.models.SlugField(db_index=True, default=mountaineer.core.utils.slug.slugid_nice, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='slug',
            field=mountaineer.core.models.SlugField(db_index=True, default=mountaineer.core.utils.slug.slugid_nice, editable=False, unique=True),
        ),
    ]