from django.db import models

from src.apps.patient.models.patient_models import Patient


class Diary(models.Model):
    content = models.TextField()
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.content


class PsychologicalConsultation(models.Model):
    content = models.TextField()
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.content


class Photo(models.Model):
    file = models.FileField(upload_to='photo/')
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
    )
