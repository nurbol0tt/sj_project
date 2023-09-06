from django.db.models import Q

from rest_framework.viewsets import ViewSet
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from drf_yasg.utils import swagger_auto_schema

from src.apps.patient.models.comment_models import Diary, PsychologicalConsultation
from src.apps.patient.serializers import (
    DiaryCreateSerializer,
    DiaryPatchSerializer,
    PsychologicalCreateSerializer,
    PsychologicalPatchSerializer,
)


class DiaryViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(request_body=DiaryCreateSerializer)
    def create(self, request):
        serializer = DiaryCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(request_body=DiaryPatchSerializer)
    def partial_update(self, request, pk=None):
        patient = get_object_or_404(Diary, id=pk)
        serializer = DiaryPatchSerializer(patient, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class PsychologicalConsultationViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(request_body=PsychologicalCreateSerializer)
    def create(self, request):
        serializer = PsychologicalCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(request_body=PsychologicalPatchSerializer)
    def partial_update(self, request, pk=None):
        patient = get_object_or_404(PsychologicalConsultation, id=pk)
        serializer = PsychologicalPatchSerializer(
            patient, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class FileViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    # @swagger_auto_schema(request_body=...)
    def create(self, request):
        ...

    # @swagger_auto_schema(request_body=...)
    def partial_update(self, request):
        ...