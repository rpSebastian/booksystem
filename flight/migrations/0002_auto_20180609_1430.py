# Generated by Django 2.0.4 on 2018-06-09 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='ticket_bought',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='flight',
            name='ticket_number',
            field=models.IntegerField(default=100),
        ),
    ]
