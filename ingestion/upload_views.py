from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .models import DataSource, RawEmissionRecord
from .file_upload import parse_sap_csv, parse_utility_csv, parse_travel_csv

class FileUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    
    def post(self, request, organization_id, source_type):
        """
        Upload CSV file for specific source type
        source_type: 'SAP', 'UTILITY', or 'TRAVEL'
        """
        file = request.FILES.get('file')
        if not file:
            return Response(
                {'error': 'No file provided'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Get or create DataSource
        data_source, created = DataSource.objects.get_or_create(
            organization_id=organization_id,
            source_type=source_type,
            ingestion_method='FILE_UPLOAD'
        )
        
        # Parse based on source type
        if source_type == 'SAP':
            records_data = parse_sap_csv(file, organization_id, data_source.id)
        elif source_type == 'UTILITY':
            records_data = parse_utility_csv(file, organization_id, data_source.id)
        elif source_type == 'TRAVEL':
            records_data = parse_travel_csv(file, organization_id, data_source.id)
        else:
            return Response(
                {'error': 'Invalid source_type. Use SAP, UTILITY, or TRAVEL'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Save all records
        saved_records = []
        for record_data in records_data:
            raw_record = RawEmissionRecord.objects.create(**record_data)
            saved_records.append({
                'id': raw_record.id,
                'row_number': raw_record.row_number
            })
        
        return Response({
            'message': f'Successfully uploaded {len(saved_records)} records',
            'source_type': source_type,
            'data_source_id': data_source.id,
            'records': saved_records
        }, status=status.HTTP_201_CREATED)