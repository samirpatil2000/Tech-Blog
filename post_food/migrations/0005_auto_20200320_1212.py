# Generated by Django 3.0.4 on 2020-03-20 12:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post_food', '0004_auto_20200320_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 20, 12, 12, 40, 713285, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
