from typing import Type, Tuple

from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ViewSet
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from drf_yasg.utils import swagger_auto_schema

from src.apps.patient.models.patient_models import Patient
from src.apps.patient.models.comment_models import (
    Diary,
    PsychologicalConsultation,
    Photo,
)
from src.apps.patient.serializers import (
    ContentSerializer,
    PhotoSerializer,
    PhotoListSerializer, PsychologicalContentSerializer,
)


class DiaryViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['POST'],)  # url_path='create-diary-entry'
    @swagger_auto_schema(request_body=ContentSerializer)
    def diary_entry(self, request, pk=None) -> Response:
        patient = get_object_or_404(Patient, id=pk)
        serializer = ContentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(patient=patient)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get'],)
    def lists(self, request, pk=None) -> Response:
        query = Diary.objects.filter(patient_id=pk)
        serializer = ContentSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None) -> Response:
        diary = get_object_or_404(Diary, id=pk)
        serializer = ContentSerializer(diary)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ContentSerializer)
    def partial_update(self, request, pk=None) -> Response:
        patient = get_object_or_404(Diary, id=pk)
        serializer = ContentSerializer(patient, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None) -> Response:
        patient = get_object_or_404(Diary, id=pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PsychologicalConsultationViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['POST'],)
    @swagger_auto_schema(request_body=PsychologicalContentSerializer)
    def psychology(self, request, pk=None) -> Response:
        patient = get_object_or_404(Patient, id=pk)
        serializer = PsychologicalContentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(patient=patient)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get'], )
    def lists(self, request, pk=None) -> Response:
        queryset = PsychologicalConsultation.objects.filter(patient_id=pk)
        print(queryset)
        serializer = PsychologicalContentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None) -> Response:
        diary = get_object_or_404(PsychologicalConsultation, id=pk)
        serializer = PsychologicalContentSerializer(diary)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ContentSerializer)
    def partial_update(self, request, pk=None) -> Response:
        patient = get_object_or_404(PsychologicalConsultation, id=pk)
        serializer = PsychologicalContentSerializer(
            patient, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None) -> Response:
        patient = get_object_or_404(PsychologicalConsultation, id=pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FileViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)
    parser_classes: Tuple[Type[MultiPartParser], Type[FormParser]] = (MultiPartParser, FormParser)

    @action(detail=True, methods=['post'],)
    @swagger_auto_schema(request_body=PhotoSerializer)
    def file(self, request, pk=None) -> Response:
        patient = get_object_or_404(Patient, id=pk)
        serializer = PhotoSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(patient=patient)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['patch'],)
    @swagger_auto_schema(request_body=PhotoSerializer)
    def patch(self, request, pk=None) -> Response:
        photo = get_object_or_404(Photo, id=pk)
        serializer = PhotoSerializer(
            photo, data=request.data, partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def retrieve(self, request, pk=None) -> Response:
        file = get_object_or_404(Photo, id=pk)
        serializer = PhotoListSerializer(file)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'],)
    def all_photo(self, request, pk=None) -> Response:
        queryset = (
            Photo.objects.filter(patient_id=pk)
            .filter(user__role=request.user.role)
        )
        serializer = PhotoListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None) -> Response:
        photo = get_object_or_404(Photo, id=pk)
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
