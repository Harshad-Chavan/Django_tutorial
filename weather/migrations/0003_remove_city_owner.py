# Generated by Django 3.0.5 on 2020-04-21 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_city_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='owner',
        ),
    ]