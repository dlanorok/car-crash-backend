# Generated by Django 3.2.18 on 2023-04-10 18:08

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drivers', '0001_initial'),
        ('crashes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('damaged_parts', multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Front'), ('2', 'Right'), ('3', 'Back'), ('5', 'Left')], max_length=3)),
                ('name', models.CharField(blank=True, default=False, max_length=128)),
                ('registration_plate', models.CharField(blank=True, max_length=8)),
                ('creator', models.CharField(blank=True, max_length=128)),
                ('crash', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crashes.crash')),
                ('driver', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='drivers.driver')),
            ],
        ),
    ]
