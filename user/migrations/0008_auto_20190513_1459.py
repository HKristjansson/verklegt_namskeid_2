# Generated by Django 2.2.1 on 2019-05-13 14:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0007_auto_20190512_2309'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CreditCard',
            new_name='Sale',
        ),
    ]
