# Generated by Django 3.0.4 on 2020-03-29 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0019_auto_20200329_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
