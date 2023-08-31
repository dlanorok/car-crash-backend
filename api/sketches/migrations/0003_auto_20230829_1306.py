# Generated by Django 3.2.18 on 2023-08-29 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crashes', '0001_initial'),
        ('files', '0001_initial'),
        ('sketches', '0002_auto_20230829_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sketch',
            name='crash',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sketch', to='crashes.crash'),
        ),
        migrations.AlterField(
            model_name='sketch',
            name='file_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sketch', to='files.file'),
        ),
    ]
