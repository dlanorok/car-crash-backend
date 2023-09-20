# Generated by Django 3.2.18 on 2023-09-20 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PolicyHolder',
            fields=[
                ('revision', models.IntegerField(default=0)),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('email_phone_number', models.CharField(blank=True, max_length=128, null=True)),
                ('address', models.CharField(blank=True, max_length=256, null=True)),
                ('country_code', models.CharField(blank=True, max_length=128, null=True)),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='policy_holder', serialize=False, to='cars.car')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
