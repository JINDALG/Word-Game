# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('wordgame', '0011_user_total_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z]{3,20}$', message='This is not a valid username')]),
        ),
    ]
