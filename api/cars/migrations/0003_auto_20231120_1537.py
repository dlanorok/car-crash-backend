# Generated by Django 3.2.18 on 2023-11-20 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20231027_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='additional_data',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='witnesses',
            field=models.TextField(blank=True, null=True),
        ),
    ]
