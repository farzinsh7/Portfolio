# Generated by Django 3.2 on 2021-04-26 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_settings', '0002_auto_20210426_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetting',
            name='instagram',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='linkedin',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='twitter',
            field=models.CharField(max_length=50),
        ),
    ]