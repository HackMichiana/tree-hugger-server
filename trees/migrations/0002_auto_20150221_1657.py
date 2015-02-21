# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tree',
            name='dead',
        ),
        migrations.AddField(
            model_name='tree',
            name='accuracy',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tree',
            name='condition',
            field=models.CharField(default=b'U', max_length=1, choices=[(b'E', b'Excellent'), (b'G', b'Good'), (b'F', b'Fair'), (b'P', b'Poor'), (b'D', b'Dying'), (b'X', b'Dead'), (b'U', b'Unknown')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tree',
            name='diameter',
            field=models.CharField(default=b'U', max_length=2, choices=[(b'Y', b'Young'), (b'E', b'Established'), (b'M', b'Maturing'), (b'MA', b'Mature'), (b'U', b'Unknown')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tree',
            name='height',
            field=models.CharField(default=b'U', max_length=1, choices=[(b'S', b'Small'), (b'M', b'Medium'), (b'L', b'Large'), (b'U', b'Unknown')]),
            preserve_default=True,
        ),
    ]
