# Generated by Django 4.0.1 on 2022-02-03 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='status',
            field=models.CharField(choices=[('U', 'Undefined'), ('C', 'Coach'), ('M', 'Manager'), ('R', 'Receptionist'), ('S', 'Student'), ('P', 'Parent')], default='Undefined', max_length=20),
        ),
    ]
