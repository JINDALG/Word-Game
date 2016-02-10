# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('wordgame', '0005_auto_20160111_0614'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='a@b.com', unique=True, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(regex='^[a-z A-Z]{3,20}$', message='This is not a valid username')]),
        ),
    ]
