# Generated by Django 2.2.1 on 2019-05-12 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190512_1803'),
    ]

    operations = [
        migrations.RenameField(
            model_name='creditcard',
            old_name='cardholder_id',
            new_name='cardholder',
        ),
    ]
