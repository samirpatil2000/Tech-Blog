# Generated by Django 2.2 on 2020-02-24 13:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post_food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 24, 13, 11, 29, 897548, tzinfo=utc)),
        ),
    ]
