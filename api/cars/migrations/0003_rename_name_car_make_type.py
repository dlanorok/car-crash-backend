# Generated by Django 3.2.18 on 2023-05-11 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_remove_car_policy_holder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='name',
            new_name='make_type',
        ),
    ]
