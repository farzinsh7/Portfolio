# Generated by Django 3.2 on 2021-04-28 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_resume', '0006_rename_categoriess_resume_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=25)),
                ('class_icon', models.CharField(max_length=30)),
            ],
        ),
    ]
