from django.db import models


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
# 
# 
# class AnamnesisDisease(models.Model):
#     # receiving_something = models.CharField(max_length=255)
#     # receiving_something_time = models.DateField(max_length=255)
#     ...
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
