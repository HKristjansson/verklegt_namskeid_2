# Generated by Django 2.2.1 on 2019-05-14 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0007_apartmentsearch_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentsearch',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apartment.ApartmentCategory'),
        ),
    ]
