# Generated by Django 2.2.1 on 2019-05-05 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('zip', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
                ('rooms', models.CharField(max_length=255)),
                ('size', models.FloatField(max_length=255)),
                ('price', models.IntegerField()),
                ('available', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ApartmentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ApartmentImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=999)),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartment.Apartment')),
            ],
        ),
        migrations.CreateModel(
            name='ApartmentDateAdded',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField()),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartment.Apartment')),
            ],
        ),
        migrations.AddField(
            model_name='apartment',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='apartment.ApartmentCategory'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='seller',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='seller.Seller'),
        ),
    ]
