# Generated by Django 2.2.1 on 2019-05-05 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='rooms',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='ApartmentDateAdded',
        ),
    ]
