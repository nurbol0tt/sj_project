from django.contrib import admin

from src.apps.patient.models.comment_models import PsychologicalConsultation, Diary, Photo
from src.apps.patient.models.emcrisis_models import Epicrisis
from src.apps.patient.models.patient_models import Patient, PatientInfo
from src.apps.patient.models.info_models import (
    SomaticStatus,
    MentalStatus,
    AnamnesisDisease
)

# Register your models here.
admin.site.register(Patient)
admin.site.register(PatientInfo)
admin.site.register(SomaticStatus)
admin.site.register(MentalStatus)
admin.site.register(Diary)
admin.site.register(PsychologicalConsultation)
admin.site.register(Photo)
admin.site.register(Epicrisis)
admin.site.register(AnamnesisDisease)
