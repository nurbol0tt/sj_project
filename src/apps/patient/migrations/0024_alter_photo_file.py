# Generated by Django 4.2.4 on 2024-01-28 15:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("patient", "0023_alter_patient_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="file",
            field=models.FileField(upload_to="api/media/photo/"),
        ),
    ]
