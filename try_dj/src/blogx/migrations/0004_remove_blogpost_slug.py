# Generated by Django 2.2 on 2020-04-08 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogx', '0003_blogpost_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='slug',
        ),
    ]
