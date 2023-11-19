from celery import shared_task
from django.utils import timezone
from .models.patient_models import PatientInfo


@shared_task
def update_patient_status():
    patient_status_true = (
        PatientInfo.objects.filter(
        date_of_discharge__gte=timezone.now()
        ).order_by('patient', '-date_of_discharge')
        .distinct('patient')
        )

    patient_status_false = (
        PatientInfo.objects.filter(
            date_of_discharge__lte=timezone.now()
        ).order_by('patient', '-date_of_discharge')
        .distinct('patient')
    )

    for patient_info_true in patient_status_true:
        patient_info_true.patient.in_hospital = True
        patient_info_true.patient.save()

    for patient_info_false in patient_status_false:
        patient_info_false.patient.in_hospital = False
        patient_info_false.patient.save()
