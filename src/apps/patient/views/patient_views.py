from django.shortcuts import render

from rest_framework.viewsets import ViewSet
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import action

from drf_yasg.utils import swagger_auto_schema

from src.apps.patient.models.patient_models import Patient, PatientInfo
from src.apps.patient.models.info_models import AnamnesisLife

from ..serializers import PatientCreateSerializer, PatientListSerializer


class PatientViewSet(ViewSet):
    # permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(request_body=PatientCreateSerializer)
    def create(self, request):
        # Handle POST request to create a new instance
        serializer = PatientCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        # Handle GET request to list all instances
        queryset = Patient.objects.all()
        serializer = PatientListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def retrieve(self, request, pk=None):
        # Handle GET request to retrieve a single instance
        patient = get_object_or_404(Patient, id=pk)
    
    @swagger_auto_schema(request_body=PatientCreateSerializer)
    def partial_update(self, request, pk=None):
        # Handle PATCH request to partially update an instance
        patient = get_object_or_404(Patient, id=pk)
        serializer = PatientCreateSerializer(patient, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        # Handle DELETE request to delete an instance
        patient = get_object_or_404(Patient, id=pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StatusListView(ViewSet):

    @action(detail=False, methods=['GET'])
    def education_list(self, request) -> Response:
        queryset = AnamnesisLife.EDUCATIONS_STATUS_CHOICES
        status_list = [{role[0]: role[1]} for role in queryset]
        return Response(status_list, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def family_list(self, request) -> Response:
        queryset = AnamnesisLife.FAMILY_STATUS_CHOICES
        status_list = [{role[0]: role[1]} for role in queryset]
        return Response(status_list, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def arrives_list(self, request) -> Response:
        queryset = PatientInfo.STATUS_CHOICES_ARRIVES
        status_list = [{role[0]: role[1]} for role in queryset]
        return Response(status_list, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def conditions_list(self, request) -> Response:
        queryset = PatientInfo.STATUS_CHOICES_CONDITIONS
        status_list = [{role[0]: role[1]} for role in queryset]
        return Response(status_list, status=status.HTTP_200_OK)
