# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='train_course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Course', models.CharField(max_length=20)),
                ('People', models.CharField(max_length=20)),
                ('Teacher', models.CharField(max_length=20)),
                ('Section', models.CharField(max_length=20)),
                ('Place', models.CharField(max_length=20)),
                ('Classes', models.CharField(max_length=20)),
                ('Week', models.CharField(max_length=20)),
            ],
        ),
    ]
