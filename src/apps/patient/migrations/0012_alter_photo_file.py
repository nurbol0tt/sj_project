# Generated by Django 4.2.4 on 2023-09-06 18:05
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('patient', '0011_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.FileField(upload_to='photo/'),
        ),
    ]
