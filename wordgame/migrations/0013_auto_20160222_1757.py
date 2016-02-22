# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('wordgame', '0012_auto_20160222_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(unique=True, max_length=20, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]{3,20}$', message='This is not a valid username')]),
        ),
    ]
