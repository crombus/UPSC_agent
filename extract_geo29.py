import json
from pathlib import Path

with open('EXPORT-PDF-STATUS.json', 'r', encoding='utf-8') as f:
    status = json.load(f)

for rec in status.get('records', []):
    if rec.get('record_id') == 'geography-29:learner-v2:g2':
        print('Record ID:', rec['record_id'])
        print('Generation:', rec.get('generation'))
        print('Approved:', rec.get('approved'))
        print('Validation state:', rec.get('validation', {}).get('state'))
        print('Main PDF:', rec.get('main_pdf'))
        print('Workbook:', rec.get('workbook'))
        break
else:
    print('Record not found')
