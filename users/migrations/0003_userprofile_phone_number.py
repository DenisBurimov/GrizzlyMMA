# Generated by Django 4.0.1 on 2022-02-03 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_userprofile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(default='YourPhone', max_length=12),
        ),
    ]
