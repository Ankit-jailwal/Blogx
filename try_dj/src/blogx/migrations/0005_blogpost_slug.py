# Generated by Django 2.2 on 2020-04-08 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogx', '0004_remove_blogpost_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default='My-Blog'),
            preserve_default=False,
        ),
    ]