# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0005_remove_train_course_week1'),
    ]

    operations = [
        migrations.CreateModel(
            name='train_basic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.CharField(max_length=20)),
                ('Pastern', models.CharField(max_length=20)),
                ('Build', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=20)),
                ('Power', models.CharField(max_length=20)),
                ('Area', models.CharField(max_length=20)),
            ],
        ),
    ]
