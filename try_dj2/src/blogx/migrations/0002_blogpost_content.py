# Generated by Django 2.2 on 2019-12-24 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogx', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
