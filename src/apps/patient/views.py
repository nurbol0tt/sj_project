from rest_framework.viewsets import ViewSet
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .serializers import PatientCreateSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status


class PatientViewSet(ViewSet):
    # permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(request_body=PatientCreateSerializer)
    def create(self, request):
        serializer = PatientCreateSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
