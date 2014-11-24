# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('igoda', '0002_auto_20141122_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoplist',
            name='shop_tel',
            field=models.CharField(max_length=15),
            preserve_default=True,
        ),
    ]
