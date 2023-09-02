from django.contrib import admin
from src.apps.patient.models.patient_models import Patient, PatientInfo
from src.apps.patient.models.info_models import (
    Category, AnamnesisDisease, TypeTolerance, TypeIntoxication, TypePalimpsests
)

# Register your models here.
admin.site.register(Patient)
admin.site.register(PatientInfo)
admin.site.register(Category)
admin.site.register(TypeTolerance)
admin.site.register(TypeIntoxication)
admin.site.register(TypePalimpsests)
