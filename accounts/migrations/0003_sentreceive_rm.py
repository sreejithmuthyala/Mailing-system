# Generated by Django 4.0.6 on 2022-08-10 10:53

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_sentreceive_receive_mails'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentreceive',
            name='rm',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None), size=None), default=[], size=None),
            preserve_default=False,
        ),
    ]
