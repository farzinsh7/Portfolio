# Generated by Django 4.2.18 on 2025-02-01 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summary',
            name='short_description',
            field=models.TextField(default='short description', max_length=300),
        ),
    ]
