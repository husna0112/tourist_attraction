# Generated by Django 3.0.4 on 2020-04-05 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0021_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='touristattraction',
            name='slug',
        ),
    ]
