# Generated by Django 2.0.5 on 2018-06-01 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0002_booking_booking_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
    ]