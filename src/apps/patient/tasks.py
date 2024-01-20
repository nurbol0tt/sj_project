from celery import shared_task
from django.db.models import Max
from django.utils import timezone
from .models.patient_models import PatientInfo


@shared_task
def update_patient_status():
    latest_discharge_dates = (
        PatientInfo.objects.values('patient')
        .annotate(
            latest_discharge=Max(
                'date_of_discharge'
            )
        )
    )
    current_datetime = timezone.now()

    for patient_info_true in latest_discharge_dates:
        patient_info_instance = PatientInfo.objects.get(pk=patient_info_true['patient'])

        if patient_info_instance.date_of_discharge and patient_info_instance.date_of_discharge < current_datetime:
            patient_info_instance.patient.in_hospital = False
        else:
            patient_info_instance.patient.in_hospital = True

        patient_info_instance.patient.save()
