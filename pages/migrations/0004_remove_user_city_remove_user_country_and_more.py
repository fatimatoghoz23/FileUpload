# Generated by Django 4.2 on 2023-09-23 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_doctor',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_patient',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pincode',
        ),
    ]