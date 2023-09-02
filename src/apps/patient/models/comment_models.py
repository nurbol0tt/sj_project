from django.db import models


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
