# Generated by Django 3.0.4 on 2020-04-18 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0023_plan_touristattractions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='touristattractions',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='user',
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
    ]
