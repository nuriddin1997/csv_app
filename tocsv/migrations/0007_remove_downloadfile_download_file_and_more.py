# Generated by Django 4.0 on 2021-12-30 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tocsv', '0006_alter_downloadfile_download_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='downloadfile',
            name='download_file',
        ),
        migrations.AddField(
            model_name='downloadfile',
            name='new_file_name',
            field=models.TextField(blank=True, max_length=50000),
        ),
    ]
