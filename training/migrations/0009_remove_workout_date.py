# Generated by Django 3.1.2 on 2020-10-24 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0008_auto_20201023_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='date',
        ),
    ]
