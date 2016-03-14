# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordgame', '0013_auto_20160222_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='total_score',
        ),
        migrations.AlterField(
            model_name='user',
            name='score',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
