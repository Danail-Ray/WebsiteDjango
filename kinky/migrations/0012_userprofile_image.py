# Generated by Django 5.0.1 on 2024-01-28 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinky', '0011_alter_userprofile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='images/'),
        ),
    ]
