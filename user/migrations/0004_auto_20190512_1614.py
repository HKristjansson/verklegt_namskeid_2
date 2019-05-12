# Generated by Django 2.2.1 on 2019-05-12 16:14

import creditcards.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_payment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.AddField(
            model_name='profile',
            name='cc_code',
            field=creditcards.models.SecurityCodeField(blank=True, default=123, max_length=4, verbose_name='security code'),
        ),
        migrations.AddField(
            model_name='profile',
            name='cc_expiry',
            field=creditcards.models.CardExpiryField(blank=True, default='01/19', verbose_name='expiration date'),
        ),
        migrations.AddField(
            model_name='profile',
            name='cc_number',
            field=creditcards.models.CardNumberField(blank=True, default=0, max_length=25, verbose_name='card number'),
        ),
    ]
