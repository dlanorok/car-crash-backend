# Generated by Django 3.2.18 on 2023-04-10 18:00

import api.crashes.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('session_id', models.CharField(default=api.crashes.models.generate_unique_code, max_length=8, null=True, unique=True)),
                ('closed', models.BooleanField(default=False)),
            ],
        ),
    ]
