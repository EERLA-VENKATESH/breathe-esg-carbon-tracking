from django.shortcuts import render

# Create your views here.



from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import (
    Organization,
    DataSource,
    RawEmissionRecord,
    NormalizedEmissionRecord,
    ReviewStatus,
    AuditLog
)
from .serializers import (
    OrganizationSerializer,
    DataSourceSerializer,
    RawEmissionRecordSerializer,
    NormalizedEmissionRecordSerializer,
    ReviewStatusSerializer,
    AuditLogSerializer
)

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class DataSourceViewSet(viewsets.ModelViewSet):
    queryset = DataSource.objects.all()
    serializer_class = DataSourceSerializer

class RawEmissionRecordViewSet(viewsets.ModelViewSet):
    queryset = RawEmissionRecord.objects.all()
    serializer_class = RawEmissionRecordSerializer

class NormalizedEmissionRecordViewSet(viewsets.ModelViewSet):
    queryset = NormalizedEmissionRecord.objects.all()
    serializer_class = NormalizedEmissionRecordSerializer

class ReviewStatusViewSet(viewsets.ModelViewSet):
    queryset = ReviewStatus.objects.all()
    serializer_class = ReviewStatusSerializer

class AuditLogViewSet(viewsets.ModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer