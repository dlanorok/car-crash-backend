# Generated by Django 3.2.18 on 2023-05-22 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='car',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='driver', serialize=False, to='cars.car'),
        ),
    ]