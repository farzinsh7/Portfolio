# Generated by Django 3.2 on 2021-04-26 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_settings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesetting',
            name='awards',
        ),
        migrations.RemoveField(
            model_name='sitesetting',
            name='clients',
        ),
        migrations.RemoveField(
            model_name='sitesetting',
            name='hours_of_supports',
        ),
        migrations.RemoveField(
            model_name='sitesetting',
            name='projects',
        ),
    ]
