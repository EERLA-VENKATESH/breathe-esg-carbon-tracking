from rest_framework import serializers
from .models import (
    Organization,
    DataSource,
    RawEmissionRecord,
    NormalizedEmissionRecord,
    ReviewStatus,
    AuditLog
)

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class DataSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSource
        fields = '__all__'

class RawEmissionRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawEmissionRecord
        fields = '__all__'

class NormalizedEmissionRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormalizedEmissionRecord
        fields = '__all__'

class ReviewStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewStatus
        fields = '__all__'

class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = '__all__'