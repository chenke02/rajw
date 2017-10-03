# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0003_remove_train_people'),
    ]

    operations = [
        migrations.AddField(
            model_name='train_course',
            name='Week1',
            field=models.CharField(default=datetime.datetime(2017, 10, 1, 18, 6, 30, 789000, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
    ]
