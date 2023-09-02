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

from ..serializers import PatientCreateSerializer, PatientRecordSerializer


class PatientRecordViewSet(ViewSet):

    @swagger_auto_schema(request_body=PatientRecordSerializer)
    def create(self, request):
        # Handle POST request to create a new instance
        serializer = PatientRecordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        # Handle GET request to retrieve a single instance
        ...

    @swagger_auto_schema(request_body=PatientCreateSerializer)
    def partial_update(self, request, pk=None):
        # Handle PATCH request to partially update an instance
        ...

    def destroy(self, request, pk=None):
        ...
