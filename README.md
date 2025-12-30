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
| `MAC_Vendors/` | Hardware manufacturer identities (OUI lookup) | 10.1M |
| `DHCP_Signatures/` | DHCP Option 55 fingerprint patterns | 368K |
| `DHCP_Vendors/` | DHCP vendor class strings | 425K |
| `Devices/` | Device profiles (phones, routers, IoT, etc.) | 116K |
| `DHCPv6_Enterprise/` | IPv6 enterprise identifiers | 58K |
| `DHCPv6_Signatures/` | IPv6 DHCP fingerprints | 1.6K |
| `Satori_Fingerprints/` | OS & protocol fingerprinting (TCP, SSH, SSL, etc.) | 1,980 |
| `Combinations/` | **Fingerprint → Device mappings** (the missing link!) | 813 |

---

## The Missing Link: Combinations

Most fingerprint databases give you raw patterns but don't tell you what device they belong to. The `Combinations/` folder bridges this gap:

```
DHCP Pattern "1,3,6,15,28,51,58,59"
        ↓
    Fingerprint ID #450
        ↓
    Device ID #9417 → "Amazon Android"
```

This mapping was built by cross-referencing [Satori](https://github.com/xnih/satori) fingerprints with our device database.

| Stat | Count |
|------|-------|
| Total mappings | 813 |
| Linked to device IDs | 727 |
| Satori-only (new devices) | 86 |

---

## Satori Fingerprints

The `Satori_Fingerprints/` folder contains OS and protocol identification signatures from the [Satori project](https://github.com/xnih/satori). Unlike DHCP fingerprinting, these identify devices by analyzing protocol behavior:

| File | Fingerprints | What It Identifies |
|------|-------------|-------------------|
| `dhcp.json` | 481 | DHCP → Device name/type |
| `webuseragent.json` | 899 | User-Agent → Browser/Device |
| `tcp.json` | 184 | TCP stack → Operating System |
| `smb.json` | 89 | SMB → Windows version |
| `ssh.json` | 67 | SSH banner → Server software |
| `web.json` | 67 | HTTP response → Web server |
| `ssl.json` | 51 | TLS handshake → Implementation |
| `dns.json` | 48 | DNS quirks → DNS server |
| `ntp.json` | 25 | NTP → Device type |
| `sip.json` | 25 | SIP → VoIP device |
| `browser.json` | 22 | Browser behavior → Browser type |
| `icmp.json` | 13 | Ping response → OS |
| `dhcpv6.json` | 9 | DHCPv6 → Device |

---

## Data Formats

Each folder contains the same data in multiple formats:

```
MAC_Vendors/
├── csv/          # Comma-separated values
├── json/         # JSON records array
├── parquet/      # Columnar format (compressed)
└── sqlite/       # SQLite database
```

| Format | Best For | Notes |
|--------|----------|-------|
| **CSV** | Excel, pandas, quick parsing | Universal compatibility |
| **JSON** | Web apps, APIs, JavaScript | Easy to parse |
| **Parquet** | Data science, Spark, fast analytics | Compressed, fast queries |
| **SQLite** | SQL queries, local databases | Single file, queryable |

Large datasets are chunked into parts to stay under GitHub's 100MB limit.

---

## Quick Start

### Python — Lookup a MAC Address
```python
import sqlite3

conn = sqlite3.connect('MAC_Vendors/sqlite/mac_vendor_part01.db')
cursor = conn.execute("SELECT name FROM mac_vendors WHERE mac = '9CE330'")
print(cursor.fetchone())  # → ('Cisco Systems, Inc.',)
```

### Python — Find Device from DHCP Fingerprint
```python
import sqlite3

# 1. Get fingerprint ID
conn = sqlite3.connect('DHCP_Signatures/sqlite/dhcp_signature.db')
cursor = conn.execute("SELECT id FROM dhcp_signatures WHERE value = '1,3,6,15,28,51,58,59'")
fp_id = cursor.fetchone()[0]

# 2. Get device from combinations
conn2 = sqlite3.connect('Combinations/sqlite/combinations.db')
cursor2 = conn2.execute("SELECT satori_name, device_type FROM dhcp_combinations WHERE dhcp_fingerprint_id = ?", (fp_id,))
print(cursor2.fetchone())  # → ('Amazon Fire OS', 'eBook Reader')
```

### Python — OS Fingerprint from TCP Behavior
```python
import json

with open('Satori_Fingerprints/json/tcp.json') as f:
    tcp_fps = json.load(f)

# Find fingerprints for Linux
linux_fps = [fp for fp in tcp_fps if 'Linux' in fp.get('os_name', '')]
print(f"Found {len(linux_fps)} Linux TCP fingerprints")
```

### JavaScript — Load Devices
```javascript
const devices = require('./Devices/json/device.json');
const iphones = devices.filter(d => d.name.includes('iPhone'));
console.log(`Found ${iphones.length} iPhone variants`);
```

---

## Use Cases

| Use Case | What You Need |
|----------|---------------|
| **"What device is this MAC?"** | `MAC_Vendors/` |
| **"What device sent this DHCP?"** | `DHCP_Signatures/` + `Combinations/` |
| **"What OS from TCP behavior?"** | `Satori_Fingerprints/tcp.json` |
| **"Identify SSH server version"** | `Satori_Fingerprints/ssh.json` |
| **"Detect browser from User-Agent"** | `Satori_Fingerprints/webuseragent.json` |
| **"Full device profile"** | `Devices/` |

---

## The Identification Chain

```
┌─────────────────────────────────────────────────────────────┐
│  NETWORK TRAFFIC                                            │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  MAC Address: 00:1A:2B:XX:XX:XX                             │
│  → MAC_Vendors/ → "Apple, Inc."                             │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  DHCP Option 55: 1,3,6,15,28,51,58,59                       │
│  → DHCP_Signatures/ → ID #450                               │
│  → Combinations/ → "Amazon Fire OS" (eBook Reader)          │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  TCP SYN: Window=65535, TTL=64, Options=MSS,NOP,WS,NOP,NOP  │
│  → Satori tcp.json → "iOS 14.x"                             │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  RESULT: Apple device running iOS 14                        │
└─────────────────────────────────────────────────────────────┘
```

---

## Data Sources

| Source | License | What It Provides |
|--------|---------|-----------------|
| [Satori](https://github.com/xnih/satori) | GPL | OS/protocol fingerprints with device mappings |
| [IEEE OUI](https://standards.ieee.org/products-programs/regauth/) | Public | Official MAC vendor registry |
| Community OSINT | ODbL 1.0 | DHCP fingerprints, devices, vendors |

---

## Repository Stats

| Metric | Value |
|--------|-------|
| Total records | ~11 million |
| Data formats | CSV, JSON, Parquet, SQLite |
| Folders | 8 |
| Last updated | December 2025 |

---

*"Thought and Memory fly each day over the spacious earth. I fear for Thought, that he come not back, yet more anxious am I for Memory."*
