from datetime import datetime

from rest_framework.viewsets import ViewSet
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.db.models import Sum


from drf_yasg.utils import swagger_auto_schema

from src.apps.patient.models.info_models import (
    AnamnesisDisease,
    SomaticStatus,
    NeurologicalStatus,

    MentalStatus,
)
from ..models.patient_models import PatientInfo, Patient

from ..serializers import (
    PatientRecordSerializer,
    AnamnesisDiseaseSerializer,
    SomaticStatusSerializer,
    NeurologicalStatusSerializer,
    MentalStatusSerializer,
    PatientPatchSerializer, 
    PatientSerializer,
    PatienRetrieveSerializer
)


class PatientRecordViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['post'])
    @swagger_auto_schema(request_body=PatientRecordSerializer)
    def record(self, request, pk=None):
        # Handle POST request to create a new instance
        patient = get_object_or_404(Patient, id=pk)
        serializer = PatientRecordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(patient=patient)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        # Handle GET request to retrieve a single instance
        record = PatientInfo.objects.filter(patient_id=pk)
        serializer = PatienRetrieveSerializer(record, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=PatientPatchSerializer)
    def partial_update(self, request, pk=None):
        record = get_object_or_404(PatientInfo, id=pk)
        serializer = PatientPatchSerializer(record, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['PATCH'])
    @swagger_auto_schema(request_body=AnamnesisDiseaseSerializer)
    def anamnesis(self, request, pk=None):
        anamnesis = get_object_or_404(AnamnesisDisease, id=pk)
        serializer = AnamnesisDiseaseSerializer(anamnesis, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    @action(detail=True, methods=['PATCH'])
    @swagger_auto_schema(request_body=SomaticStatusSerializer)
    def somatic(self, request, pk=None):
        somatic = get_object_or_404(SomaticStatus, id=pk)
        serializer = SomaticStatusSerializer(somatic, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    @action(detail=True, methods=['PATCH'])
    @swagger_auto_schema(request_body=NeurologicalStatusSerializer)
    def neurological(self, request, pk=None):
        somatic = get_object_or_404(NeurologicalStatus, id=pk)
        serializer = NeurologicalStatusSerializer(somatic, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    @action(detail=True, methods=['PATCH'])
    @swagger_auto_schema(request_body=MentalStatusSerializer)
    def mental(self, request, pk=None):
        somatic = get_object_or_404(MentalStatus, id=pk)
        serializer = MentalStatusSerializer(somatic, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class MonthlyIncomeViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        current_year = datetime.now().year

        # Initialize a dictionary to store monthly incomes
        monthly_incomes = {}

        # Iterate through the months starting from September of the current year
        for year in range(2024, current_year + 1):  # Calculate for the current year and the next year
            start_month = 1 if year == current_year else 1  # Start from September for the current year
            end_month = 12 if year == current_year else 12  # End in December for both years

            for month in range(start_month, end_month + 1):
                # Filter PatientInfo instances for the specified year and month
                income_data = PatientInfo.objects.filter(
                    date_of_admission__year=year,
                    date_of_admission__month=month
                ).aggregate(total_income=Sum('price'))

                # Extract the total income for the month
                total_income = income_data['total_income'] or 0

                # Store the income in the dictionary
                monthly_incomes[f"{year}-{month:02d}"] = total_income

        return Response(monthly_incomes)

    @action(detail=False, methods=['get'])
    def lists(self, request) -> Response:
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
