# Generated by Django 3.2.18 on 2023-10-25 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='driving_licence_category',
            field=models.CharField(max_length=256, null=True),
        ),
    ]