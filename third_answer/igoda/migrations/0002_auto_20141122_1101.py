# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('igoda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoplist',
            name='shop_tel',
            field=models.IntegerField(max_length=15),
            preserve_default=True,
        ),
    ]
