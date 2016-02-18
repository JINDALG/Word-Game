# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordgame', '0006_auto_20160205_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='image_url',
            field=models.ImageField(upload_to='img'),
        ),
    ]
