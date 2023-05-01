# Generated by Django 3.2.18 on 2023-04-28 12:33

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_car_initial_impact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='damaged_parts',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Front'), ('2', 'Right'), ('3', 'Back'), ('5', 'Left')], max_length=3),
        ),
        migrations.AlterField(
            model_name='car',
            name='initial_impact',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Front'), ('2', 'Right'), ('3', 'Back'), ('5', 'Left')], max_length=3),
        ),
    ]
