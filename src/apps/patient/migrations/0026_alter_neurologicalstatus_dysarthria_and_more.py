# Generated by Django 4.2.4 on 2024-02-09 17:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("patient", "0025_alter_anamnesisdisease_last_treatment_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="neurologicalstatus",
            name="dysarthria",
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name="neurologicalstatus",
            name="meningeal_signs",
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name="neurologicalstatus",
            name="photo_reaction",
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name="neurologicalstatus",
            name="seizures",
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name="somaticstatus",
            name="traces",
            field=models.CharField(max_length=25),
        ),
    ]
