import json
from pathlib import Path

status_file = Path('EXPORT-PDF-STATUS.json')
if status_file.exists():
    with open(status_file, 'r', encoding='utf-8') as f:
        status = json.load(f)
    
    print(f'Total records: {len(status.get("records", []))}')
    
    # Find all geography-29 records
    geo29_records = [r for r in status.get('records', []) if 'geography-29' in r.get('record_id', '')]
    
    if geo29_records:
        print(f'\nFound {len(geo29_records)} geography-29 record(s):')
        for rec in geo29_records:
            print(f"- {rec.get('record_id')}: approved={rec.get('approved')}, validation={rec.get('validation', {}).get('state')}")
            print(f"  Main PDF: {rec.get('main_pdf', 'N/A')}")
            print(f"  Workbook: {rec.get('workbook', 'N/A')}")
    else:
        print('\nNo geography-29 records found')
        # Show last 5 records for debugging
        print('\nLast 5 records:')
        for rec in status.get('records', [])[-5:]:
            print(f"- {rec.get('record_id')}")
else:
    print('EXPORT-PDF-STATUS.json not found')
