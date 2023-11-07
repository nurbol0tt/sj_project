from django.db import models

from src.apps.patient.models.patient_models import Patient


class Epicrisis(models.Model):  # noqa
    start_treatment = models.DateField()
    end_treatment = models.DateField()
    main_diagnosis = models.CharField(max_length=255)
    concomitant = models.CharField(max_length=125)
    complications = models.CharField(max_length=255)
    laboratory_tests = models.CharField(max_length=255)
    instrumental_studies = models.CharField(max_length=255)
    ecg = models.CharField(max_length=255)
    x_ray = models.CharField(max_length=125)
    specialist_consultations = models.CharField(max_length=255)
    treatment = models.CharField(max_length=255)
    treatment_results = models.CharField(max_length=125)
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
    )
    recommendations = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
