# Generated by Django 4.2.4 on 2023-08-25 17:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0003_delete_patient"),
        ("patient", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="AnamnesisLife",
        ),
    ]
