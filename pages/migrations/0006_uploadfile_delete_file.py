# Generated by Django 4.2 on 2023-09-23 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_file_remove_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='photos/%y/%m/%d')),
            ],
        ),
        migrations.DeleteModel(
            name='file',
        ),
    ]