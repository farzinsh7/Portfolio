# Generated by Django 3.2 on 2021-04-28 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_resume', '0002_auto_20210428_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='name',
            field=models.CharField(default=None, max_length=200),
        ),
    ]