from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import (
    Organization,
    DataSource,
    RawEmissionRecord,
    NormalizedEmissionRecord,
    ReviewStatus,
    AuditLog
)

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)

@admin.register(DataSource)
class DataSourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'organization', 'source_type', 'ingestion_method', 'created_at')
    list_filter = ('source_type', 'ingestion_method')
    search_fields = ('organization__name',)

@admin.register(RawEmissionRecord)
class RawEmissionRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'organization', 'source', 'ingestion_timestamp')
    list_filter = ('source__source_type',)
    search_fields = ('organization__name',)

@admin.register(NormalizedEmissionRecord)
class NormalizedEmissionRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'organization', 'scope', 'category', 'activity_value', 'unit', 'calculated_emissions', 'period_start', 'period_end')
    list_filter = ('scope', 'category')
    search_fields = ('organization__name',)

@admin.register(ReviewStatus)
class ReviewStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'record', 'status', 'analyst', 'reviewed_at')
    list_filter = ('status',)
    search_fields = ('record__id',)

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'record', 'action', 'performed_by', 'timestamp')
    list_filter = ('action',)
    search_fields = ('record__id',)
