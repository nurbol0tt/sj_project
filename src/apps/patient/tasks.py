from celery import shared_task
from django.utils import timezone
from .models.patient_models import PatientInfo


@shared_task
def update_patient_status():
    # Query PatientInfo objects and update associated Patient objects
    now = timezone.now()
    (PatientInfo.objects
     .filter(date_of_discharge__lte=now)
     .update(patient__in_hospital=False)
     )


# @shared_task
# def update_in_hospital_status():
#     now = datetime.now()
#     patients_to_update = PatientInfo.objects.filter(
#         date_of_discharge__lte=now,
#         patient__in_hospital=True
#     )
#
#     for patient_info in patients_to_update:
#         patient_info.patient.in_hospital = False
#         patient_info.patient.save()
