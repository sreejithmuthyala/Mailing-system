# Generated by Django 4.0.6 on 2022-08-11 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_sentreceive_sm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sentreceive',
            name='receive_mails',
        ),
        migrations.RemoveField(
            model_name='sentreceive',
            name='sent_mails',
        ),
    ]
