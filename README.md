# Huginn & Muninn

![Huginn & Muninn](Hugiin_Muniin.jpg)

> *"Every day Huginn and Muninn fly over the vast earth. I fear for Huginn that he may not return, but I fear even more for Muninn."*
> — Odin, from the Grímnismál

In Norse mythology, **Huginn** (thought) and **Muninn** (memory) are Odin's two ravens. Each day they fly across Midgard, observing everything, then return to whisper all they've seen and heard into Odin's ear.

This repository is the knowledge the ravens have gathered — scouring the internet for crumbs of device intelligence, network signatures, and hardware identities. They report back what they find.

---

## The Ravens' Findings

| Folder | What the Ravens Found | Records |
|--------|----------------------|---------|
| `MAC_Vendors/` | Hardware manufacturer identities | 10.1M |
| `DHCP_Signatures/` | Network request patterns → device/OS | 368K |
| `DHCP_Vendors/` | Device vendor strings | 425K |
| `Devices/` | Device profiles (phones, consoles, routers, etc.) | 116K |
| `DHCPv6_Enterprise/` | IPv6 enterprise identifiers | 58K |
| `DHCPv6_Signatures/` | IPv6 network signatures | 1.6K |

---

## Data Formats

Each folder contains the same data in multiple formats:

```
Devices/
├── csv/          # Comma-separated values
├── json/         # JSON records array
├── parquet/      # Columnar format (compressed)
└── sqlite/       # SQLite database
```

| Format | Best For | Size |
|--------|----------|------|
| **CSV** | Excel, pandas, quick parsing | 941 MB |
| **JSON** | Web apps, APIs, JavaScript | 217 MB |
| **Parquet** | Data science, Spark, fast analytics | 316 MB |
| **SQLite** | SQL queries, local databases | 113 MB |

Large tables (MAC_Vendors, DHCP_Vendors) are chunked into parts to stay under 100MB.

---

## Quick Start

### Python — Load MAC Vendors
```python
import csv
import glob

mac_vendors = {}
for part in glob.glob('MAC_Vendors/csv/mac_vendor_part*.csv'):
    with open(part, 'r') as f:
        for row in csv.DictReader(f):
            mac_vendors[row['mac']] = row['name']

# Lookup
print(mac_vendors.get('9CE330', 'Unknown'))  # → Cisco
```

### Python — Query SQLite
```python
import sqlite3

conn = sqlite3.connect('Devices/sqlite/device.db')
for row in conn.execute("SELECT name FROM device WHERE name LIKE '%iPhone%'"):
    print(row[0])
```

### Python — Load Parquet (fastest)
```python
import pandas as pd

df = pd.read_parquet('Devices/parquet/device.parquet')
iphones = df[df['name'].str.contains('iPhone')]
print(iphones)
```

### JavaScript — Load JSON
```javascript
const devices = require('./Devices/json/device.json');
const iphones = devices.filter(d => d.name.includes('iPhone'));
```

---

## Use Cases

- **Network Reconnaissance** — Identify devices on any network
- **Asset Discovery** — Catalog all connected hardware
- **Threat Detection** — Spot rogue or spoofed devices
- **BYOD Classification** — Sort personal vs corporate devices
- **Security Research** — Know what's out there

---

## The Ravens Report

Like Odin's ravens returning at dusk, this database brings you knowledge:

| When a device... | The ravens tell you... |
|------------------|------------------------|
| Joins a network | Device type, OS, manufacturer |
| Shows its MAC | Who made it |
| Sends vendor strings | What it claims to be |

---

## Data Source

Internet crowdsourced OSINT under the [Open Database License (ODbL 1.0)](https://opendatacommons.org/licenses/odbl/).

---

## License

Open data for network security, research, and educational purposes.

---

*"Thought and Memory fly each day over the spacious earth. I fear for Thought, that he come not back, yet more anxious am I for Memory."*
