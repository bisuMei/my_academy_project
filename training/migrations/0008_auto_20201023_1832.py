# Generated by Django 3.1.2 on 2020-10-24 01:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0007_auto_20201023_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
