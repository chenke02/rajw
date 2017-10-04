# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0002_train_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='train_basic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.CharField(max_length=20)),
                ('Category', models.CharField(max_length=20)),
                ('Pastern', models.CharField(max_length=20)),
                ('Build', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=20)),
                ('Content', models.CharField(max_length=20)),
                ('Power', models.CharField(max_length=20)),
                ('Length', models.IntegerField(max_length=5)),
                ('Width', models.IntegerField(max_length=5)),
                ('Remarks', models.CharField(max_length=20)),
            ],
        ),
    ]
