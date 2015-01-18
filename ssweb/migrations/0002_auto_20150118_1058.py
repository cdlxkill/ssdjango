# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ssweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='ss_port',
            field=models.IntegerField(default=9630, unique=True),
            preserve_default=True,
        ),
    ]
