# Generated by Django 3.2.18 on 2023-09-06 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_alter_car_responsibility_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='responsibility_type',
            field=models.CharField(blank=True, choices=[('ME', 'me'), ('ANOTHER', 'another'), ('UNKNOWN', 'unknown')], default='', max_length=100),
            preserve_default=False,
        ),
    ]