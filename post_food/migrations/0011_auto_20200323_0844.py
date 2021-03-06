# Generated by Django 3.0.4 on 2020-03-23 08:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post_food', '0010_auto_20200323_0625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='post_food.Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 23, 8, 44, 47, 155680, tzinfo=utc)),
        ),
    ]
