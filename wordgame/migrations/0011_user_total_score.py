# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordgame', '0010_auto_20160218_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='total_score',
            field=models.CharField(default='0', max_length=500),
        ),
    ]
