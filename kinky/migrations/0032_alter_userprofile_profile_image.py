# Generated by Django 5.0.1 on 2024-01-31 13:44

import kinky.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinky', '0031_alter_userprofile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, default='', null=True, upload_to=kinky.models.user_image_upload_path),
        ),
    ]
