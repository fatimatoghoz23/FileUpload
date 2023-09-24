# Generated by Django 4.2 on 2023-09-23 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_uploadfile_delete_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='image',
            field=models.FileField(upload_to='media/%y/%m/%d'),
        ),
    ]