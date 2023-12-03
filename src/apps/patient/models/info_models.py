from django.db import models


class AnamnesisLife(models.Model):
    EDUCATIONS_STATUS_CHOICES = (
        ('1', 'Высшее'),
        ('2', 'Средне-специальные'),
        ('3', 'Среднее'),
        ('4', 'Неполное среднее'),
        ('5', 'Начальное'),
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
        'Patient',
        on_delete=models.CASCADE,
        related_name='anamnesis_life'
    )
    
    def __str__(self) -> str:
        return self.patient


class AnamnesisDisease(models.Model):
    receiving_something = models.CharField(max_length=255)
    receiving_something_time = models.DateField(max_length=255)
    somatic_disorders = models.CharField(max_length=255)
    mental_disorders = models.CharField(max_length=255)
    daily_tolerance = models.FloatField()
    binge_drinking = models.CharField(max_length=25)
    light_gaps = models.CharField(max_length=25)
    duration_last_binge = models.CharField(max_length=25)
    duration_last_remission = models.CharField(max_length=25)
    last_treatment = models.CharField(max_length=25)
    last_alcohol_intake = models.CharField(max_length=25)
    dose = models.CharField(max_length=25)
    addition = models.CharField(max_length=125)
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    category = models.CharField(max_length=255)
    type_tolerance = models.CharField(max_length=255)
    type_intoxication = models.CharField(max_length=255)
    type_palimpsests = models.CharField(max_length=255)


class SomaticStatus(models.Model):
    CONDITION_STATUS_CHOICES = (
        ('1', 'Удовлетворительное'),
        ('2', 'Средней тяжести'),
        ('3', 'Тяжелое'),
        ('4', 'Крайне тяжелое'),
    )
    CATEGORY_STATUS_CHOICES = (
        ('1', 'Пониженного'),
        ('2', 'Повышенного питания'),
        ('3', 'Истощен'),
        ('4', 'Крайне тяжелое'),
    )
    SKIN_TYPE_STATUS_CHOICES = (
        ('1', 'Обычные цвета'),
        ('2', 'Цианотические'),
        ('3', 'Акроцианоз'),
        ('4', 'Мраморные'),
        ('5', 'Бледные'),
        ('6', 'Гиперимированные'),
        ('7', 'Сухие'),
        ('8', 'Влажные'),
    )
    AVAILABILITY_STATUS_CHOICES = (
        ('1', 'Наличие шрамов'),
        ('2', 'Садин'),
        ('3', 'Ушибов'),
        ('4', 'Гематом'),
        ('5', 'Парезов'),
        ('6', 'Воспаления'),
        ('7', 'Сухие'),
        ('8', 'Влажные'),
    )
    TRACES_STATUS_CHOICES = (
        ('1', 'Наличие шрамов'),
        ('2', 'Ссадин'),
        ('3', 'Ушибов'),
        ('4', 'Гематом'),
        ('5', 'Парезов'),
        ('6', 'Воспаления'),
    )
    CONJUNCTIVA_STATUS_CHOICES = (
        ('1', 'Блеск глаз'),
        ('2', 'Гиперимия'),
        ('3', 'Икретичность'),
    )
    WHEEZING_STATUS_CHOICES = (
        ('1', 'Хрипы нет'),
        ('2', 'Хрипы есть')
    )
    HEART_TONES_STATUS_CHOICES = (
        ('1', 'Тоны ясные'),
        ('2', 'Приглушены'),
        ('3', 'Глухие'),
        ('4', 'Аритмичные'),
    )
    condition = models.CharField(
        max_length=25,
        choices=CONDITION_STATUS_CHOICES,
    )
    category = models.CharField(
        max_length=25,
        choices=CATEGORY_STATUS_CHOICES,
    )
    skin_type = models.CharField(
        max_length=25,
        choices=SKIN_TYPE_STATUS_CHOICES,
    )
    availability = models.CharField(
        max_length=25,
        choices=AVAILABILITY_STATUS_CHOICES,
    )
    traces = models.CharField(
        max_length=25,
        choices=TRACES_STATUS_CHOICES,
    )
    state_conjunctiva = models.CharField(
        max_length=25,
        choices=CONJUNCTIVA_STATUS_CHOICES,
    )
    breath = models.CharField(
        max_length=25,
    )
    wheezing = models.CharField(
        max_length=25,
        choices=WHEEZING_STATUS_CHOICES,
    )
    bh = models.CharField(max_length=25,)
    saturation = models.CharField(max_length=25)
    heart_tones = models.CharField(
        max_length=25,
        choices=HEART_TONES_STATUS_CHOICES,
    )
    ad = models.CharField(max_length=25,)
    pulse_frequency = models.FloatField()
    filling = models.CharField(
        max_length=25,
        choices=HEART_TONES_STATUS_CHOICES,
    )
    tongue = models.CharField(
        max_length=125, blank=True, null=True
    )
    stomach = models.CharField(
        max_length=125, blank=True, null=True
    )
    liver = models.CharField(
        max_length=125, blank=True, null=True
    )
    vomiting = models.CharField(
        max_length=125, blank=True, null=True
    )
    stool = models.CharField(
        max_length=125, blank=True, null=True
    )
    diuresis = models.CharField(
        max_length=125, blank=True, null=True
    )
    edema = models.CharField(
        max_length=125, blank=True, null=True
    )
    glucose = models.CharField(
        max_length=125, blank=True, null=True
    )
    apparatus = models.CharField(
        max_length=125, blank=True, null=True
    )
    vascular_system = models.CharField(max_length=125,)
    supplements = models.CharField(
        max_length=125, blank=True, null=True
    )


class NeurologicalStatus(models.Model):
    PUPILS_STATUS_CHOICES = (
        ('1', 'Нистагм'),
        ('2', 'Мидриаз'),
        ('3', 'Миоз'),
        ('4', 'Анизокория'),
    )
    MENINGEAL_STATUS_CHOICES = (
        ('1', 'Ригидность затылочных мышц'),
        ('2', 'Симптом Кернинга'),
        ('3', 'Брудзинского'),
    )
    pupils = models.CharField(
        max_length=25,
        choices=PUPILS_STATUS_CHOICES,
    )
    photo_reaction = models.CharField(
        max_length=25,
    )
    meningeal_signs = models.CharField(
        max_length=25,
        choices=MENINGEAL_STATUS_CHOICES,
    )
    seizures = models.CharField(
        max_length=25,
    )
    dysarthria = models.CharField(
        max_length=25
    )


class MentalStatus(models.Model):
    VIEW_STATUS_CHOICES = (
        ('1', 'Вид опрятен'),
        ('2', 'Вид не опрятен')
    )
    view = models.CharField(
        max_length=25,
        choices=VIEW_STATUS_CHOICES,
    )
    smell_of_alcohol = models.BooleanField()
    behavior = models.CharField(max_length=125,)
    consciousness = models.CharField(max_length=125,)
    orientation = models.CharField(max_length=125,)
    perception_disorders = models.CharField(max_length=125,)
    emotional_background = models.CharField(max_length=125,)
    night_sleep = models.CharField(max_length=125,)
    suicide_attempt = models.CharField(max_length=125,)
    causes_of_alcohol = models.CharField(max_length=125,)
    purpose_of_hospitalization = models.CharField(max_length=125,)
