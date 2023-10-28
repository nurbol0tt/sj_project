from typing import Type, Tuple

from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ViewSet
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from drf_yasg.utils import swagger_auto_schema

from src.apps.patient.models.emcrisis_models import Epicrisis
from src.apps.patient.models.patient_models import Patient
from src.apps.patient.serializers import EpicrisisSerializer, EpicrisisSerializerList, EpicrisisDetailSerializer


class EpicrisisViewSet(ViewSet):  # noqa

    @action(detail=True, methods=['POST'],)
    @swagger_auto_schema(request_body=EpicrisisSerializer)
    def post(self, request, pk=None) -> Response:
        patient = get_object_or_404(Patient, id=pk)
        serializer = EpicrisisSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(patient=patient)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['POST'],)
    def lists(self, request, pk=None):
        epicrisis = Epicrisis.objects.filter(patient_id=pk)  # noqa
        serializer = EpicrisisSerializerList(epicrisis, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        epicrisis = get_object_or_404(Epicrisis, id=pk)
        serializer = EpicrisisDetailSerializer(epicrisis)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=EpicrisisSerializer)
    def partial_update(self, request, pk=None) -> Response:
        epicrisis = get_object_or_404(Epicrisis, id=pk)
        serializer = EpicrisisSerializer(epicrisis, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None) -> Response:
        patient = get_object_or_404(Epicrisis, id=pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
