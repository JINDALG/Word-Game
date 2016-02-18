# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordgame', '0007_auto_20160217_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='image_url',
            field=models.ImageField(upload_to='img/'),
        ),
    ]
