# Generated by Django 3.0.4 on 2020-03-08 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TouristAttraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('detail', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
