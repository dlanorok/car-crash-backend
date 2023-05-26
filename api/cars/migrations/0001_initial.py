# Generated by Django 3.2.18 on 2023-05-16 08:47

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crashes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revision', models.IntegerField(default=0)),
                ('creator', models.CharField(blank=True, max_length=128)),
                ('car_type', models.CharField(blank=True, max_length=128)),
                ('make_type', models.CharField(blank=True, max_length=128)),
                ('registration_country', models.CharField(blank=True, max_length=256)),
                ('registration_plate', models.CharField(blank=True, max_length=256)),
                ('damaged_parts', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Front'), ('2', 'Right'), ('3', 'Back'), ('5', 'Left')], max_length=3)),
                ('initial_impact', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Front'), ('2', 'Right'), ('3', 'Back'), ('5', 'Left')], max_length=3)),
                ('crash', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='crashes.crash')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]