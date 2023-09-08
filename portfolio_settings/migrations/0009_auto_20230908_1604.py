# Generated by Django 3.2 on 2023-09-08 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_settings', '0008_services'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesetting',
            name='github',
        ),
        migrations.RemoveField(
            model_name='sitesetting',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='sitesetting',
            name='linkedin',
        ),
        migrations.CreateModel(
            name='SocialMedias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('icon', models.CharField(max_length=200, null=True)),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('site_setting', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='socials', to='portfolio_settings.sitesetting')),
            ],
        ),
    ]