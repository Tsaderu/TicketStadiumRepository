# Generated by Django 4.1.3 on 2022-11-28 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProfilesApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='orders',
        ),
    ]
