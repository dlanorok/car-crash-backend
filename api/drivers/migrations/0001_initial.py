# Generated by Django 3.2.18 on 2023-04-10 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128)),
                ('surname', models.CharField(blank=True, max_length=128)),
                ('email', models.CharField(blank=True, max_length=128)),
                ('address', models.CharField(blank=True, max_length=256)),
                ('post_number', models.CharField(blank=True, max_length=256)),
                ('country_code', models.CharField(blank=True, max_length=128)),
            ],
        ),
    ]
