# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0002_auto_20150221_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='')),
                ('type', models.CharField(max_length=1, default='tree', choices=[('T', 'Tree'), ('L', 'Leaf')])),
                ('tree', models.ForeignKey(to='trees.Tree')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='tree',
            name='condition',
            field=models.CharField(max_length=1, default='U', choices=[('E', 'Excellent'), ('G', 'Good'), ('F', 'Fair'), ('P', 'Poor'), ('D', 'Dying'), ('X', 'Dead'), ('U', 'Unknown')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tree',
            name='diameter',
            field=models.CharField(max_length=2, default='U', choices=[('Y', 'Young'), ('E', 'Established'), ('M', 'Maturing'), ('MA', 'Mature'), ('U', 'Unknown')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tree',
            name='height',
            field=models.CharField(max_length=1, default='U', choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('U', 'Unknown')]),
            preserve_default=True,
        ),
    ]
