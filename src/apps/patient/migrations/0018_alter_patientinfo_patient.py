# Generated by Django 4.2.4 on 2023-11-07 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("patient", "0017_patient_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patientinfo",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="patient_info",
                to="patient.patient",
            ),
        ),
    ]
