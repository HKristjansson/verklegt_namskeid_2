# Generated by Django 2.2.1 on 2019-05-13 15:39

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20190513_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now().date),
            preserve_default=False,
        ),
    ]