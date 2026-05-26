from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RawEmissionRecord, NormalizedEmissionRecord
from decimal import Decimal

class NormalizeRecordsView(APIView):
    def post(self, request, organization_id):
        raw_records = RawEmissionRecord.objects.filter(
            organization_id=organization_id,
            normalizedemissionrecord__isnull=True  # Only unprocessed
        )
        
        normalized_count = 0
        for raw_record in raw_records:
            # Simple normalization logic
            # For SAP records with German headers
            raw_data = raw_record.raw_data
            
            # Extract values (handle German headers)
            activity_value = Decimal(str(raw_data.get('Menge', 0)))
            unit = raw_data.get('ME', 'L')
            date_str = raw_data.get('Datum', '')
            
            # Simple emission factor (in real app, lookup from database)
            emission_factor = Decimal('0.0025')  # Example: 2.5 kg CO2e per unit
            
            # Calculate emissions (tCO2e)
            calculated_emissions = activity_value * emission_factor / Decimal('1000')
            
            # Create normalized record
            NormalizedEmissionRecord.objects.create(
                organization_id=organization_id,
                raw_record=raw_record,
                scope=1,  # Scope 1 for fuel combustion
                category='fuel_combustion',
                activity_value=activity_value,
                unit='kg',  # Normalized unit
                emission_factor=emission_factor,
                calculated_emissions=calculated_emissions,
                period_start='2024-01-01',
                period_end='2024-12-31'
            )
            normalized_count += 1
        
        return Response({
            'message': f'Normalized {normalized_count} records',
            'total_raw': raw_records.count(),
            'normalized': normalized_count
        }, status=status.HTTP_200_OK)