# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 11:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0003_auto_20160528_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='created_at',
            field=models.DateField(default=datetime.date(2016, 5, 29), verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
    ]