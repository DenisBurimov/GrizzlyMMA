# Generated by Django 4.0.1 on 2022-02-12 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0006_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=20)),
                ('coach', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='coaches.manager')),
            ],
        ),
    ]
