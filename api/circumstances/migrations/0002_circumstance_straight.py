# Generated by Django 3.2.18 on 2023-10-04 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circumstances', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='circumstance',
            name='straight',
            field=models.BooleanField(default=False),
        ),
    ]