# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0003_auto_20150221_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='accuracy',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
