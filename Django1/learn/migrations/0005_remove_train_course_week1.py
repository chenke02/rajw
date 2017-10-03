# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0004_train_course_week1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='train_course',
            name='Week1',
        ),
    ]
