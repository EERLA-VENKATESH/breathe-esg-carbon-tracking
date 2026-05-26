from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import NormalizedEmissionRecord, ReviewStatus, AuditLog

class ApproveRecordView(APIView):
    def post(self, request, record_id, analyst_id=None):
        try:
            record = NormalizedEmissionRecord.objects.get(id=record_id)
            analyst = User.objects.get(id=analyst_id) if analyst_id else request.user
            
            # Create or update review status
            review_status, created = ReviewStatus.objects.get_or_create(record=record)
            review_status.status = 'APPROVED'
            review_status.analyst = analyst
            review_status.notes = request.data.get('notes', '')
            review_status.save()
            
            # Create audit log
            AuditLog.objects.create(
                record=record,
                action='APPROVE',
                new_state={'status': 'APPROVED'},
                performed_by=analyst
            )
            
            return Response({
                'message': 'Record approved successfully',
                'record_id': record_id,
                'status': 'APPROVED'
            })
            
        except NormalizedEmissionRecord.DoesNotExist:
            return Response({'error': 'Record not found'}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({'error': 'Analyst not found'}, status=status.HTTP_404_NOT_FOUND)

class FlagRecordView(APIView):
    def post(self, request, record_id, analyst_id=None):
        try:
            record = NormalizedEmissionRecord.objects.get(id=record_id)
            analyst = User.objects.get(id=analyst_id) if analyst_id else request.user
            
            review_status, created = ReviewStatus.objects.get_or_create(record=record)
            review_status.status = 'FLAGGED'
            review_status.analyst = analyst
            review_status.notes = request.data.get('notes', 'Flagged for review')
            review_status.save()
            
            AuditLog.objects.create(
                record=record,
                action='FLAG',
                new_state={'status': 'FLAGGED', 'notes': review_status.notes},
                performed_by=analyst
            )
            
            return Response({
                'message': 'Record flagged successfully',
                'record_id': record_id,
                'status': 'FLAGGED'
            })
            
        except NormalizedEmissionRecord.DoesNotExist:
            return Response({'error': 'Record not found'}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({'error': 'Analyst not found'}, status=status.HTTP_404_NOT_FOUND)

class ReviewDashboardView(APIView):
    def get(self, request, organization_id):
        pending = ReviewStatus.objects.filter(
            record__organization_id=organization_id,
            status='PENDING'
        ).count()
        
        flagged = ReviewStatus.objects.filter(
            record__organization_id=organization_id,
            status='FLAGGED'
        ).count()
        
        approved = ReviewStatus.objects.filter(
            record__organization_id=organization_id,
            status='APPROVED'
        ).count()
        
        rejected = ReviewStatus.objects.filter(
            record__organization_id=organization_id,
            status='REJECTED'
        ).count()
        
        return Response({
            'organization_id': organization_id,
            'summary': {
                'pending': pending,
                'flagged': flagged,
                'approved': approved,
                'rejected': rejected,
                'total': pending + flagged + approved + rejected
            }
        })