# Generated by Django 2.2.1 on 2019-05-12 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20190512_1804'),
    ]

    operations = [
        migrations.RenameField(
            model_name='creditcard',
            old_name='cardholder',
            new_name='cardholder_id',
        ),
    ]
