# Generated by Django 2.2.1 on 2019-05-11 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('apartment', '0003_apartment_buyer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='buyer',
        ),
        migrations.AddField(
            model_name='apartment',
            name='buyer_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='user.Profile'),
            preserve_default=False,
        ),
    ]
