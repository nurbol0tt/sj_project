# Generated by Django 4.2.4 on 2024-02-06 16:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("patient", "0024_alter_photo_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="anamnesisdisease",
            name="last_treatment",
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name="mentalstatus",
            name="smell_of_alcohol",
            field=models.CharField(max_length=125),
        ),
        migrations.AlterField(
            model_name="neurologicalstatus",
            name="pupils",
            field=models.CharField(
                choices=[
                    ("1", "Нистагм"),
                    ("2", "Мидриаз"),
                    ("3", "Миоз"),
                    ("4", "Анизокория"),
                    ("5", "D=S"),
                ],
                max_length=25,
            ),
        ),
        migrations.AlterField(
            model_name="somaticstatus",
            name="availability",
            field=models.CharField(max_length=128),
        ),
    ]
