# Generated by Django 2.2 on 2020-05-22 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogx', '0013_blogpost_slug2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='slug2',
        ),
    ]
