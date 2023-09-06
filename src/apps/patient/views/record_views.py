from rest_framework.viewsets import ViewSet
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

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
        serializer = PatientRecordSerializer(record, many=True)
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
