# Generated by Django 3.2.18 on 2023-11-06 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy_holders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='policyholder',
            name='surname',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]