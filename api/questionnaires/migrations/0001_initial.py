# Generated by Django 3.2.18 on 2023-07-19 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revision', models.IntegerField(default=0)),
                ('questions', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
