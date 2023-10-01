from django.db import models
from .info_models import AnamnesisDisease, SomaticStatus, NeurologicalStatus, MentalStatus


class Patient(models.Model):
    name = models.CharField(max_length=150, blank=True,)
    surname = models.CharField(max_length=150, blank=True,)
    patronymic = models.CharField(max_length=150, blank=True,)
    date_of_birth = models.DateField(max_length=255)
    avatar = models.FileField(default='./default_png.jpg')
    in_hospital = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class PatientInfo(models.Model):
    STATUS_CHOICES_ARRIVES = (
        ('1', 'Впервые в жизни'),
        ('2', 'Впервые в данном году'),
        ('3', 'Повторно в данном году'),
        ('4', 'Повторно вообще'),
    )
    STATUS_CHOICES_CONDITIONS = (
        ('1', 'В состоянии алкольного опьянения'),
        ('2', 'Алкольного делирия'),
        ('3', 'Состоянии отмены алкоголя'),
        ('4', 'Состоянии отмены судорогами от алкоголя'),
        ('5', 'Others'),
    )
    arrives = models.CharField(
        max_length=125,
        choices=STATUS_CHOICES_ARRIVES
    )
    conditions = models.CharField(
        max_length=125
    )
    price = models.IntegerField()
    escorts = models.CharField(max_length=125)
    complaints = models.CharField(max_length=125)
    date_of_admission = models.DateTimeField()
    date_of_discharge = models.DateTimeField()
    departament = models.IntegerField()
    number_of_days = models.IntegerField()
    blood_type = models.CharField(max_length=25)
    # 1
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )
    anamnesis = models.ForeignKey(
        AnamnesisDisease,
        on_delete=models.CASCADE
    )
    somatic = models.ForeignKey(
        SomaticStatus,
        on_delete=models.CASCADE
    )
    neurological = models.ForeignKey(
        NeurologicalStatus,
        on_delete=models.CASCADE
    )
    mental = models.ForeignKey(
        MentalStatus,
        on_delete=models.CASCADE
    )
