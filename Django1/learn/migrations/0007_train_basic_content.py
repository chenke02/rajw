# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0006_train_basic'),
    ]

    operations = [
        migrations.AddField(
            model_name='train_basic',
            name='Content',
            field=models.CharField(default=datetime.datetime(2017, 10, 3, 12, 55, 40, 776000, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
    ]
