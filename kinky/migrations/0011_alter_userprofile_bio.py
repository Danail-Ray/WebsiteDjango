# Generated by Django 5.0.1 on 2024-01-28 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinky', '0010_alter_userprofile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, default='A bio has not been set yet...'),
        ),
    ]
