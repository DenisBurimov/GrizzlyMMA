# Generated by Django 4.0.1 on 2022-02-09 08:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0012_remove_userprofile_children_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Manager',
        ),
    ]
