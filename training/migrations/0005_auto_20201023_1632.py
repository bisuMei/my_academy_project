# Generated by Django 3.1.2 on 2020-10-23 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0004_auto_20201023_1623'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': (('can_add_workout', 'Can add workout'),)},
        ),
    ]
