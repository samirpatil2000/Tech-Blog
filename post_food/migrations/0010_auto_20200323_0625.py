# Generated by Django 3.0.4 on 2020-03-23 06:25

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post_food', '0009_auto_20200321_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='post_food.Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 23, 6, 24, 55, 608982, tzinfo=utc)),
        ),
    ]
