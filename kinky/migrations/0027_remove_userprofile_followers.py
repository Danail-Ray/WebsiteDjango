# Generated by Django 5.0.1 on 2024-01-30 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kinky', '0026_userprofile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='followers',
        ),
    ]
