# Generated by Django 3.2.18 on 2023-08-29 10:23

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
                ('participants_count', models.IntegerField(default=2)),
                ('car_type', models.CharField(blank=True, max_length=128)),
                ('make_type', models.CharField(blank=True, max_length=128)),
                ('registration_country', models.CharField(blank=True, max_length=256)),
                ('registration_plate', models.CharField(blank=True, max_length=256)),
                ('damaged_parts', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('front_bumper', 'FRONT_BUMPER'), ('front_hood', 'FRONT_HOOD'), ('front_windshield', 'FRONT_WINDSHIELD'), ('roof', 'ROOF'), ('left_front_doors', 'LEFT_FRONT_DOORS'), ('left_rear_doors', 'LEFT_REAR_DOORS'), ('right_rear_doors', 'RIGHT_REAR_DOORS'), ('right_front_doors', 'RIGHT_FRONT_DOORS'), ('left_front_lamp', 'LEFT_FRONT_LAMP'), ('right_front_lamp', 'RIGHT_FRONT_LAMP'), ('right_front_bumper', 'RIGHT_FRONT_BUMPER'), ('left_front_bumper', 'LEFT_FRONT_BUMPER'), ('left_rear_bumper', 'LEFT_REAR_BUMPER'), ('right_rear_bumper', 'RIGHT_REAR_BUMPER'), ('left_outside_mirror', 'LEFT_OUTSIDE_MIRROR'), ('right_outside_mirror', 'RIGHT_OUTSIDE_MIRROR'), ('rear_windshield', 'REAR_WINDSHIELD'), ('trunk', 'TRUNK'), ('right_rear_wheel', 'RIGHT_REAR_WHEEL'), ('left_rear_wheel', 'LEFT_REAR_WHEEL'), ('right_front_wheel', 'RIGHT_FRONT_WHEEL'), ('left_front_wheel', 'LEFT_FRONT_WHEEL'), ('left_rear_lamp', 'LEFT_REAR_LAMP'), ('right_rear_lamp', 'RIGHT_REAR_LAMP')], max_length=20)),
                ('initial_impact', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24')], max_length=20)),
                ('crash', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='crashes.crash')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
