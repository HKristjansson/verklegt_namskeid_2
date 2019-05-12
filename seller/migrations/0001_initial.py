# Generated by Django 2.2.1 on 2019-05-12 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.CharField(blank=True, max_length=2999)),
                ('year_of_start', models.DateTimeField()),
                ('disabled', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='SellerImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=2999)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Seller')),
            ],
        ),
    ]
