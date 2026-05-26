from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# Multi-tenant organization
class Organization(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Source tracking
class DataSource(models.Model):
    SOURCE_TYPES = [
        ('SAP', 'SAP ERP'),
        ('UTILITY', 'Utility Portal'),
        ('TRAVEL', 'Travel System'),
    ]
    INGESTION_METHODS = [
        ('FILE_UPLOAD', 'File Upload'),
        ('API_PULL', 'API Pull'),
        ('MANUAL', 'Manual Entry'),
    ]
    
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    source_type = models.CharField(max_length=20, choices=SOURCE_TYPES)
    ingestion_method = models.CharField(max_length=20, choices=INGESTION_METHODS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.organization.name} - {self.source_type}"

# Raw ingested data (before normalization)
class RawEmissionRecord(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    source = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    raw_data = models.JSONField()  # Store the original row
    file_name = models.CharField(max_length=500, null=True, blank=True)
    row_number = models.IntegerField(null=True, blank=True)
    ingestion_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Raw record {self.id} from {self.source.source_type}"

# Normalized emission records
class NormalizedEmissionRecord(models.Model):
    SCOPE_CHOICES = [
        (1, 'Scope 1'),
        (2, 'Scope 2'),
        (3, 'Scope 3'),
    ]
    
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    raw_record = models.ForeignKey(RawEmissionRecord, on_delete=models.CASCADE)
    scope = models.IntegerField(choices=SCOPE_CHOICES)
    category = models.CharField(max_length=100)
    activity_value = models.DecimalField(max_digits=20, decimal_places=6)
    unit = models.CharField(max_length=20)
    emission_factor = models.DecimalField(max_digits=20, decimal_places=10)
    calculated_emissions = models.DecimalField(max_digits=20, decimal_places=6)
    period_start = models.DateField()
    period_end = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Record {self.id} - Scope {self.scope} - {self.calculated_emissions} tCO2e"

# Review workflow
class ReviewStatus(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending Review'),
        ('FLAGGED', 'Flagged - Needs Investigation'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]
    
    record = models.ForeignKey(NormalizedEmissionRecord, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    analyst = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    notes = models.TextField(blank=True)
    reviewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Record {self.record.id} - {self.status}"

# Audit trail
class AuditLog(models.Model):
    ACTION_CHOICES = [
        ('CREATE', 'Created'),
        ('UPDATE', 'Updated'),
        ('APPROVE', 'Approved'),
        ('FLAG', 'Flagged'),
        ('REJECT', 'Rejected'),
    ]
    
    record = models.ForeignKey(NormalizedEmissionRecord, on_delete=models.CASCADE)
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    previous_state = models.JSONField(null=True, blank=True)
    new_state = models.JSONField(null=True, blank=True)
    performed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} on record {self.record.id} at {self.timestamp}"
