# Generated by Django 4.2.4 on 2023-08-25 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("patient", "0002_delete_anamnesislife"),
    ]

    operations = [
        migrations.CreateModel(
            name="AnamnesisLife",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "education",
                    models.CharField(
                        choices=[
                            ("1", "Higher"),
                            ("2", "Specialized Secondary"),
                            ("3", "Secondary"),
                            ("4", "Incomplete Secondary"),
                            ("4", "Primary"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "martial_status",
                    models.CharField(
                        choices=[
                            ("1", "Женат"),
                            ("2", "Замужем"),
                            ("3", "Разведен(а)"),
                            ("4", "Вдовец"),
                            ("5", "Вдова"),
                            ("6", "Холост"),
                            ("7", "Не замужем"),
                        ],
                        max_length=20,
                    ),
                ),
                ("place_work", models.CharField(max_length=125)),
                ("criminal_record", models.CharField(max_length=125)),
                ("previous_illnesses", models.CharField(max_length=125)),
                ("medications", models.CharField(max_length=125)),
                ("allergic_history", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=150)),
                ("surname", models.CharField(blank=True, max_length=150)),
                ("patronymic", models.CharField(blank=True, max_length=150)),
                ("date_of_birth", models.DateField(max_length=255)),
                (
                    "anamnesis_life",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patient.anamnesislife",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PatientInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "arrives",
                    models.CharField(
                        choices=[
                            ("1", "Впервые в жизни"),
                            ("2", "Впервые в данном году"),
                            ("3", "Повторно в данном году"),
                            ("4", "Повторно вообще"),
                        ],
                        max_length=125,
                    ),
                ),
                (
                    "conditions",
                    models.CharField(
                        choices=[
                            ("1", "В состоянии алкольного опьянения"),
                            ("2", "Алкольного делирия"),
                            ("3", "Состоянии отмены алкоголя"),
                            ("4", "Состоянии отмены судорогами от алкоголя"),
                            ("5", "Others"),
                        ],
                        max_length=125,
                    ),
                ),
                ("escorts", models.CharField(max_length=125)),
                ("complaints", models.CharField(max_length=125)),
                ("date_of_admission", models.DateTimeField()),
                ("date_of_discharge", models.DateTimeField()),
                ("departament", models.IntegerField()),
                ("number_of_days", models.IntegerField()),
                ("blood_type", models.CharField(max_length=25)),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patient.patient",
                    ),
                ),
            ],
        ),
    ]
