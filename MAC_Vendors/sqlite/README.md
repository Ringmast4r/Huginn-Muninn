# SQLite Format

MAC Vendors SQLite (918MB) exceeds GitHub's 100MB limit.

Generate from CSV if needed:
```python
import csv
import sqlite3

conn = sqlite3.connect('mac_vendor.db')
conn.execute('CREATE TABLE mac_vendor (id TEXT, mac TEXT, name TEXT, created_at TEXT, updated_at TEXT)')

for i in range(1, 12):
    with open(f'../csv/mac_vendor_part{i:02d}.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            conn.execute('INSERT INTO mac_vendor VALUES (?,?,?,?,?)',
                        (row['id'], row['mac'], row['name'], row['created_at'], row['updated_at']))
    conn.commit()
conn.close()
```
