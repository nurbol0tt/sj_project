from django.db import models
from src.apps.patient.models.patient_models import Patient


class AnamnesisLife(models.Model):
    EDUCATIONS_STATUS_CHOICES = (
        ('1', 'Higher'),
        ('2', 'Specialized Secondary'),
        ('3', 'Secondary'),
        ('4', 'Incomplete Secondary'),
        ('4', 'Primary'),
    )
    FAMILY_STATUS_CHOICES = (
        ('1', 'Женат'),
        ('2', 'Замужем'),
        ('3', 'Разведен(а)'),
        ('4', 'Вдовец'),
        ('5', 'Вдова'),
        ('6', 'Холост'),
        ('7', 'Не замужем'),
    )
    education = models.CharField(
        max_length=20,
        choices=EDUCATIONS_STATUS_CHOICES,
    )
    martial_status = models.CharField(
        max_length=20,
        choices=FAMILY_STATUS_CHOICES,
    )
    place_work = models.CharField(max_length=125)
    criminal_record = models.CharField(max_length=125)
    previous_illnesses = models.CharField(max_length=125)
    medications = models.CharField(max_length=125)
    allergic_history = models.CharField(max_length=255)
    patient = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
        related_name='anamnesis_life'
    )


# class AnamnesisDisease(models.Model):
#     receiving_something = models.CharField(max_length=255)
#     receiving_something_time = models.DateField(max_length=255)
#     somatic_disorders = models.CharField(max_length=255)
#     mental_disorders = models.CharField(max_length=255)
#     daily_tolerance = models.CharField(max_length=25)
#     binge_drinking = models.CharField(max_length=25)
#     light_gaps = models.CharField(max_length=255)
#     duration_last_binge = models.CharField(max_length=255)
#     duration_last_remission = models.CharField(max_length=255)
#     last_treatment = models.DateField()
#     last_alcohol_intake = models.CharField(max_length=255)
#     dose = models.CharField(max_length=25)
#     addition = models.CharField(max_length=255)
#     patient = models.ForeignKey(
#         Patient,
#         on_delete=models.CASCADE,
#     )
# 
# 
# class SomaticStatus(models.Model):
#     ...
# 
# 
# class NeurologicalStatus(models.Model):
#     ...
# 
# 
# class MentalStatus(models.Model):
#     ...
