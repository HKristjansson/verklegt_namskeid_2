# Generated by Django 2.2.1 on 2019-05-12 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20190512_2308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='creditcard',
            old_name='cardholder_id',
            new_name='cardholder',
        ),
    ]