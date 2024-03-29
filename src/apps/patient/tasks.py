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
    for patient_info_true in latest_discharge_dates:
        patient_info_instance = (
            PatientInfo.objects
            .filter(patient=patient_info_true['patient'])
            .first()
        )
        latest_patient_info = (
            PatientInfo.objects
            .filter(patient=patient_info_instance.patient)
            .latest('date_of_discharge')
        )
        if latest_patient_info.date_of_discharge < timezone.now():
            latest_patient_info.patient.in_hospital = False
        else:
            latest_patient_info.patient.in_hospital = True

        latest_patient_info.patient.save()


