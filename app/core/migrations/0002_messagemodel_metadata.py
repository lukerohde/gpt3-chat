# Generated by Django 3.1.14 on 2023-05-05 05:17

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagemodel',
            name='metadata',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
    ]
