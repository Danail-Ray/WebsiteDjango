# Generated by Django 5.0.1 on 2024-01-30 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kinky', '0024_userprofile_image_counter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagesfromuser',
            name='image_counter',
        ),
    ]
