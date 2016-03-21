# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordgame', '0008_auto_20160218_0729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='question',
            new_name='word',
        ),
    ]
