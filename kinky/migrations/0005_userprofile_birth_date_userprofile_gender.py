# Generated by Django 4.2.9 on 2024-01-26 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinky', '0004_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='', max_length=1),
        ),
    ]
