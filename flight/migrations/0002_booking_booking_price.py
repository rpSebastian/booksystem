# Generated by Django 2.0.5 on 2018-05-31 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_price',
            field=models.FloatField(default=0),
        ),
    ]
