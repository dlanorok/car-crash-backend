# Generated by Django 3.2.18 on 2023-10-27 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='additional_data',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='car',
            name='witnesses',
            field=models.TextField(blank=True),
        ),
    ]
