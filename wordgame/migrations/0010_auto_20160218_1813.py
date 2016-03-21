# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordgame', '0009_auto_20160218_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='main_word',
        ),
        migrations.AddField(
            model_name='quiz',
            name='phrase',
            field=models.CharField(default='hhh', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quiz',
            name='word',
            field=models.CharField(max_length=20),
        ),
    ]
