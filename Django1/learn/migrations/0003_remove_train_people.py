# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0002_train'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='train',
            name='People',
        ),
    ]
