# Generated by Django 3.1.2 on 2020-10-24 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0005_auto_20201023_1632'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': (('add_workout', 'Can add workout'),)},
        ),
    ]
