from django.contrib import admin

from src.apps.patient.models.comment_models import PsychologicalConsultation, Diary
from src.apps.patient.models.patient_models import Patient, PatientInfo
from src.apps.patient.models.info_models import (
    Category,
    TypeTolerance,
    TypeIntoxication,
    TypePalimpsests,
    SomaticStatus,
    MentalStatus
)

# Register your models here.
admin.site.register(Patient)
admin.site.register(PatientInfo)
admin.site.register(Category)
admin.site.register(TypeTolerance)
admin.site.register(TypeIntoxication)
admin.site.register(TypePalimpsests)
admin.site.register(SomaticStatus)
admin.site.register(MentalStatus)
admin.site.register(Diary)
admin.site.register(PsychologicalConsultation)
