# Generated by Django 3.0.4 on 2020-03-15 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0006_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('detail', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, max_length=255, null=True, upload_to='news')),
            ],
        ),
    ]
