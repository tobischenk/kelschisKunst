# Generated by Django 4.2.10 on 2024-02-08 22:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_baseimage_started_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='baseimage',
            old_name='image',
            new_name='file',
        ),
        migrations.AlterField(
            model_name='baseimage',
            name='started_at',
            field=models.DateField(default=datetime.datetime(2023, 10, 19, 22, 2, 49, 196907, tzinfo=datetime.timezone.utc)),
        ),
    ]