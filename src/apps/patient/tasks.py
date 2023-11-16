from celery import shared_task
from django.utils import timezone
from .models.patient_models import PatientInfo


@shared_task
def update_patient_status():
    # Query PatientInfo objects and update associated Patient objects
    latest_patient_info_list = (
        PatientInfo.objects.filter(
        date_of_discharge__gte=timezone.now()
        ).order_by('patient', '-date_of_discharge')
        .distinct('patient')
        )
    print(latest_patient_info_list)

    for latest_patient_info in latest_patient_info_list:
        latest_patient_info.patient.in_hospital = True
        latest_patient_info.patient.save()
