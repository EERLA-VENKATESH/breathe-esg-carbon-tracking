import csv
import json
from decimal import Decimal
from datetime import datetime
from io import TextIOWrapper
from django.core.files.uploadedfile import UploadedFile

def parse_sap_csv(file: UploadedFile, organization_id: int, source_id: int):
    """Parse SAP CSV with German headers"""
    decoded_file = TextIOWrapper(file, encoding='utf-8')
    reader = csv.DictReader(decoded_file)
    
    records = []
    for row in reader:
        # Map German headers to English
        record = {
            'organization_id': organization_id,
            'source_id': source_id,
            'raw_data': row,
            'file_name': file.name,
            'row_number': reader.line_num
        }
        records.append(record)
    return records

def parse_utility_csv(file: UploadedFile, organization_id: int, source_id: int):
    """Parse Utility meter reading CSV"""
    decoded_file = TextIOWrapper(file, encoding='utf-8')
    reader = csv.DictReader(decoded_file)
    
    records = []
    for row in reader:
        record = {
            'organization_id': organization_id,
            'source_id': source_id,
            'raw_data': row,
            'file_name': file.name,
            'row_number': reader.line_num
        }
        records.append(record)
    return records

def parse_travel_csv(file: UploadedFile, organization_id: int, source_id: int):
    """Parse Travel CSV (Concur export)"""
    decoded_file = TextIOWrapper(file, encoding='utf-8')
    reader = csv.DictReader(decoded_file)
    
    records = []
    for row in reader:
        record = {
            'organization_id': organization_id,
            'source_id': source_id,
            'raw_data': row,
            'file_name': file.name,
            'row_number': reader.line_num
        }
        records.append(record)
    return records