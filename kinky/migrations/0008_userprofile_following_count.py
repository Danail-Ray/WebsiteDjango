# Generated by Django 5.0.1 on 2024-01-28 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinky', '0007_rename_kinky_user_userprofile_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='following_count',
            field=models.IntegerField(default=0),
        ),
    ]
