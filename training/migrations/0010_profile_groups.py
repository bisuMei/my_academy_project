# Generated by Django 3.1.2 on 2020-10-26 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('training', '0009_remove_workout_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='groups',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
    ]
