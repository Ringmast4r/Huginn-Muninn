# JSON Format

MAC Vendors JSON files exceed GitHub's 100MB limit.

Generate from CSV if needed:
```python
import csv
import json

records = []
for i in range(1, 12):
    with open(f'../csv/mac_vendor_part{i:02d}.csv', 'r') as f:
        records.extend(list(csv.DictReader(f)))

with open('mac_vendor.json', 'w') as f:
    json.dump(records, f)
```
