from celery import shared_task
from django.core.exceptions import ObjectDoesNotExist
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
    print("1", latest_discharge_dates)
    for patient_info_true in latest_discharge_dates:
        try:
            patient_info_instance = PatientInfo.objects.get(pk=patient_info_true['patient'])
            print("2", patient_info_instance)
            latest_patient_info = (
                PatientInfo.objects
                .filter(patient=patient_info_instance.patient)
                .latest('date_of_discharge')
            )
            print("3", latest_patient_info)
            if patient_info_instance.date_of_discharge < timezone.now():
                print("=============================")
                patient_info_instance.patient.in_hospital = False
            else:
                print("********************************")
                patient_info_instance.patient.in_hospital = True

            patient_info_instance.patient.save()

        except ObjectDoesNotExist:
            pass
