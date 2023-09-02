from django.db import models


class Epicrisis(models.Model):
    VIEW_STATUS_CHOICES = (
        ('1', 'Выздоровление'),
        ('2', 'Улучшение'),
        ('3', 'Без изменений'),
        ('4', 'Ухудшение'),
    )
    start_treatment = models.DateField()
    end_treatment = models.DateField()
    diagnosis = models.CharField(max_length=255, blank=True, null=True)
    concomitant = models.CharField(max_length=255, blank=True, null=True)
    complications = models.CharField(max_length=255, blank=True, null=True)
    laboratory_tests = models.CharField(max_length=255, blank=True, null=True)
    instrumental_studies = models.CharField(max_length=255, blank=True, null=True)
    ecg = models.CharField(max_length=255, blank=True, null=True)
    x_ray = models.CharField(max_length=255, blank=True, null=True)
    specialist_consultations = models.CharField(max_length=255, blank=True, null=True)
    treatment = models.CharField(max_length=255, blank=True, null=True)
    treatment_results = models.CharField(
        max_length=5,
        choices=VIEW_STATUS_CHOICES
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
    )
    recommendations = models.CharField(max_length=255, blank=True, null=True)
