# Generated by Django 2.2.1 on 2019-05-14 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0010_auto_20190514_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartmentsearch',
            name='property',
        ),
    ]
