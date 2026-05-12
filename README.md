<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:000000,100:6B7280&height=220&section=header&text=HUGINN%20MUNINN&fontSize=70&fontColor=ffffff&animation=twinkling&fontAlignY=35&desc=11.3M%20records%20%7C%208%20datasets%20%7C%20device%20fingerprint%20intelligence&descSize=18&descAlignY=58"/>

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=22&pause=1000&color=FFFFFF&center=true&vCenter=true&multiline=true&repeat=true&width=950&height=80&lines=Thought+%26+Memory+%E2%80%94+Odin's+two+ravens.;MAC+%2B+DHCP+%2B+DHCPv6+%2B+protocol+behavior.;11%2C300%2C000%2B+device-intelligence+records)](https://git.io/typing-svg)

<br>

[![Records](https://img.shields.io/badge/Records-11.3M-FFFFFF?style=for-the-badge&logo=database&logoColor=000000)](#-stats---live)
[![Datasets](https://img.shields.io/badge/Datasets-8-E5E7EB?style=for-the-badge&logo=files&logoColor=000000)](#-ls-folders)
[![Formats](https://img.shields.io/badge/Formats-4-D1D5DB?style=for-the-badge&logo=fileformat&logoColor=000000)](#-formats)
[![Updates](https://img.shields.io/badge/Updates-Monthly_Auto-9CA3AF?style=for-the-badge&logo=githubactions&logoColor=000000)](#-update_schedule)
[![License](https://img.shields.io/badge/License-MIT-FFFFFF?style=for-the-badge&logo=opensourceinitiative&logoColor=000000)](#-license)

[![Stars](https://img.shields.io/github/stars/Ringmast4r/Huginn-Muninn?style=flat-square&color=FFFFFF&label=%E2%98%85%20Stars&labelColor=000000)](https://github.com/Ringmast4r/Huginn-Muninn/stargazers)
[![Forks](https://img.shields.io/github/forks/Ringmast4r/Huginn-Muninn?style=flat-square&color=E5E7EB&label=%E2%9A%A1%20Forks&labelColor=000000)](https://github.com/Ringmast4r/Huginn-Muninn/network/members)
[![Repo Size](https://img.shields.io/github/repo-size/Ringmast4r/Huginn-Muninn?style=flat-square&color=D1D5DB&labelColor=000000)](#)
[![Last Commit](https://img.shields.io/github/last-commit/Ringmast4r/Huginn-Muninn?style=flat-square&color=9CA3AF&labelColor=000000)](https://github.com/Ringmast4r/Huginn-Muninn/commits/main)
[![Visitors](https://visitor-badge.laobi.icu/badge?page_id=Ringmast4r.Huginn-Muninn)](#)

<img src="Hugiin_Muniin.jpg" alt="Huginn & Muninn" width="320">

---

## `> what_is_this`

```bash
ringmast4r@github:~$ cat huginn-muninn.txt

  PURPOSE:        Device fingerprint intelligence — every layer of identification
  SCOPE:          MAC vendor + DHCP + DHCPv6 + protocol behavior signatures
  COVERAGE:       11.3M records across 8 cross-referenced datasets
  FORMATS:        CSV, JSON, Parquet, SQLite (chunked under 100MB)
  UPDATES:        First of every month via auto-pipeline
  USE CASES:      Wardriving | Network forensics | IoT discovery | Threat intel

  STATUS:         [ LIVE & AUTO-UPDATING ]
```

> In Norse mythology, **Huginn** (thought) and **Muninn** (memory) are Odin's two ravens.
> Each day they fly across Midgard, observing everything, then return to whisper all they
> have seen into the Allfather's ear. This repository is what the ravens have gathered.

Most fingerprint databases pick *one* layer of identification. Huginn & Muninn merges
all of them into a single cross-referenced knowledge base.

---

## `> stats --live`

<div align="center">

| METRIC | COUNT | NOTES |
|:------:|:-----:|:-----:|
| **MAC Vendors** | `10,233,053` | OUI + MA-M + MA-S blocks |
| **DHCP Fingerprints** | `448,002` | Option 55 parameter request patterns |
| **DHCP Vendors** | `444,126` | Option 60 vendor class strings |
| **Device Profiles** | `119,028` | Manufacturer + model + OS + category |
| **DHCPv6 Enterprise** | `58,405` | IANA enterprise identifiers |
| **DHCPv6 Fingerprints** | `1,654` | IPv6 option-list patterns |
| **Combinations** | `813` | Fingerprint → device mappings (the bridge) |
| **Web User-Agent** | `899` | User-Agent → browser/device |
| **Total Records** | `~11.3M` | Cross-referenced across 8 datasets |

</div>

---

## `> the_missing_link` — Combinations

Most fingerprint databases give you raw patterns but don't tell you *what device they belong to*.
The `Combinations/` folder bridges this gap by linking protocol fingerprints to actual devices.

```
DHCP Pattern "1,3,6,15,28,51,58,59"
        ↓
    Fingerprint ID #450
        ↓
    Device ID #9417 → "Amazon Fire OS" (eBook Reader)
```

<div align="center">

| STAT | COUNT |
|:-----|:-----:|
| Total mappings | `813` |
| Linked to device IDs | `727` |
| Protocol-only (new devices) | `86` |

</div>

---

## `> protocol_fingerprints`

The `Satori_Fingerprints/` folder identifies devices by **how they behave** at the protocol
level, not just what they self-report. A device doesn't need to tell you it's running Linux —
its TCP stack betrays it.

<div align="center">

```mermaid
%%{init: {'theme':'dark', 'themeVariables': {'pie1':'#FFFFFF','pie2':'#E5E7EB','pie3':'#D1D5DB','pie4':'#9CA3AF','pie5':'#6B7280','pie6':'#4B5563','pie7':'#374151','pie8':'#1F2937','pie9':'#FFD700','pie10':'#9FEF00','pie11':'#FF6B6B','pie12':'#8B5CF6','pie13':'#00D4FF','pieTitleTextSize':'16px','pieLegendTextSize':'12px'}}}%%
pie showData
    title Protocol Behavior Fingerprints (1,980 total)
    "Web User-Agent" : 899
    "DHCP behavior" : 481
    "TCP stack" : 184
    "SMB handshake" : 89
    "SSH banner" : 67
    "HTTP server" : 67
    "SSL/TLS" : 51
    "DNS quirks" : 48
    "NTP" : 25
    "SIP/VoIP" : 25
    "Browser JS" : 22
    "ICMP" : 13
    "DHCPv6" : 9
```

</div>

<details>
<summary><b>Full protocol fingerprint table (13 protocols)</b></summary>

| FILE | COUNT | WHAT IT IDENTIFIES |
|:-----|:-----:|:-------------------|
| `webuseragent.json` | `899` | Browser + device from HTTP User-Agent |
| `dhcp.json` | `481` | Device name/type from DHCP behavior |
| `tcp.json` | `184` | OS from TCP stack (window, TTL, options) |
| `smb.json` | `89` | Windows version from SMB handshake |
| `ssh.json` | `67` | Server software from SSH banner |
| `web.json` | `67` | Web server from HTTP response headers |
| `ssl.json` | `51` | TLS implementation from handshake |
| `dns.json` | `48` | DNS server from query quirks |
| `ntp.json` | `25` | Device type from NTP response |
| `sip.json` | `25` | VoIP device from SIP headers |
| `browser.json` | `22` | Browser from JS execution behavior |
| `icmp.json` | `13` | OS from ICMP echo characteristics |
| `dhcpv6.json` | `9` | Device from DHCPv6 behavior |

</details>

---

## `> identification_chain`

```
┌─────────────────────────────────────────────────────────────┐
│  NETWORK TRAFFIC OBSERVED                                   │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  MAC: 00:1A:2B:XX:XX:XX                                     │
│  → MAC_Vendors/      → "Apple, Inc."                        │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  DHCP Option 55: 1,3,6,15,28,51,58,59                       │
│  → DHCP_Signatures/  → fingerprint ID #450                  │
│  → Combinations/     → "Amazon Fire OS" (eBook Reader)      │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  TCP SYN: Window=65535, TTL=64, Options=MSS,NOP,WS,NOP,NOP  │
│  → tcp.json          → "iOS 14.x"                           │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  RESULT: Apple device running iOS 14 + Amazon Fire OS app   │
└─────────────────────────────────────────────────────────────┘
```

---

## `> ls folders/`

<div align="center">

| FOLDER | WHAT IT HOLDS | RECORDS | FORMATS |
|:-------|:--------------|:-------:|:-------:|
| `MAC_Vendors/` | Hardware manufacturer identities (OUI extended) | `10.2M` | csv/json/parquet/sqlite |
| `DHCP_Signatures/` | DHCP Option 55 fingerprint patterns | `448K` | csv/json/parquet/sqlite |
| `DHCP_Vendors/` | DHCP Option 60 vendor class strings | `444K` | csv/json/parquet/sqlite |
| `Devices/` | Full device profiles | `119K` | csv/json/parquet/sqlite |
| `DHCPv6_Enterprise/` | IPv6 IANA enterprise identifiers | `58K` | csv/json/parquet/sqlite |
| `DHCPv6_Signatures/` | IPv6 DHCP fingerprints | `1.6K` | csv/json/parquet/sqlite |
| `Satori_Fingerprints/` | Protocol behavior signatures (13 protocols) | `1,980` | csv/json/sqlite/xml |

| `Combinations/` | Fingerprint → device mappings (the bridge) | `813` | csv/json/sqlite |

</div>

---

## `> formats`

Each folder ships the same data in multiple formats. Pick the one that fits your stack.

<div align="center">

| FORMAT | BEST FOR | NOTES |
|:------:|:---------|:------|
| ![CSV](https://img.shields.io/badge/CSV-Universal-FFFFFF?style=flat-square&labelColor=000000) | Excel, pandas, quick parsing | Plain text, universal |
| ![JSON](https://img.shields.io/badge/JSON-API_Friendly-E5E7EB?style=flat-square&labelColor=000000) | Web apps, JavaScript, REST | Easy to load |
| ![Parquet](https://img.shields.io/badge/Parquet-Analytics-D1D5DB?style=flat-square&labelColor=000000) | Spark, Polars, DuckDB | Columnar, compressed |
| ![SQLite](https://img.shields.io/badge/SQLite-Indexed-9CA3AF?style=flat-square&labelColor=000000&logo=sqlite&logoColor=000000) | SQL queries, local DBs | Single file, queryable |

</div>

Large datasets are chunked under GitHub's **100 MB per-file limit** (e.g. `mac_vendor_part01.csv` … `mac_vendor_part11.csv`).

---

## `> usage`

### `python` — Lookup a MAC

```python
import sqlite3

conn = sqlite3.connect('MAC_Vendors/sqlite/mac_vendor_part01.db')
row = conn.execute(
    "SELECT name FROM mac_vendor WHERE mac = '9CE330'"
).fetchone()
print(row)  # → ('Cisco Systems, Inc.',)
```

### `python` — Find Device from DHCP Fingerprint

```python
import sqlite3

# 1. Get fingerprint ID
sig = sqlite3.connect('DHCP_Signatures/sqlite/dhcp_fingerprint.db')
fp_id = sig.execute(
    "SELECT id FROM dhcp_fingerprint WHERE value = '1,3,6,15,28,51,58,59'"
).fetchone()[0]

# 2. Cross-reference with combinations
comb = sqlite3.connect('Combinations/sqlite/dhcp_combinations.db')
row = comb.execute(
    "SELECT satori_name, device_type FROM dhcp_combinations WHERE dhcp_fingerprint_id = ?",
    (fp_id,)
).fetchone()
print(row)  # → ('Amazon Fire OS', 'eBook Reader')
```

### `python` — OS from TCP Behavior

```python
import json

with open('Satori_Fingerprints/json/tcp.json') as f:
    tcp_fps = json.load(f)

linux = [fp for fp in tcp_fps if 'Linux' in fp.get('os_name', '')]
print(f"{len(linux)} Linux TCP fingerprints")
```

### `node.js`

```javascript
const devices = require('./Devices/json/device.json');
const iphones = devices.filter(d => d.name.includes('iPhone'));
console.log(`${iphones.length} iPhone variants`);
```

### `duckdb` — Query Parquet directly

```sql
SELECT name, COUNT(*)
FROM 'MAC_Vendors/parquet/mac_vendor_part*.parquet'
GROUP BY name
ORDER BY 2 DESC
LIMIT 20;
```

---

## `> use_cases`

```mermaid
%%{init: {'theme':'dark', 'themeVariables': {'pie1':'#FFFFFF','pie2':'#E5E7EB','pie3':'#D1D5DB','pie4':'#9CA3AF','pie5':'#FFD700','pie6':'#9FEF00','pieTitleTextSize':'16px','pieLegendTextSize':'12px'}}}%%
pie showData
    title Who Uses This (and How)
    "Wardriving / WiFi mapping" : 28
    "Network forensics & IR" : 22
    "IoT / asset discovery" : 18
    "Threat intel pipelines" : 14
    "Educational / classroom" : 10
    "Spoofing detection" : 8
```

<div align="center">

| USE CASE | DATASETS YOU NEED |
|:---------|:------------------|
| **"What device is this MAC?"** | `MAC_Vendors/` |
| **"What device sent this DHCP?"** | `DHCP_Signatures/` + `Combinations/` |
| **"What OS from TCP behavior?"** | `Satori_Fingerprints/tcp.json` |
| **"Identify SSH server version"** | `Satori_Fingerprints/ssh.json` |
| **"Detect browser from User-Agent"** | `Satori_Fingerprints/webuseragent.json` |
| **"Full device profile by ID"** | `Devices/` |
| **"IPv6 device identification"** | `DHCPv6_Signatures/` + `DHCPv6_Enterprise/` |

</div>

---

## `> update_schedule`

The repo auto-updates on the **first of every month** at `03:00 UTC` via an internal pipeline.
The data is *additive* — devices don't disappear and fingerprints don't go stale fast, so
monthly refresh is the right cadence.

---

## `> related_projects`

[![OUI Master DB](https://img.shields.io/badge/OUI_Master_Database-88K_Vendors-FFFFFF?style=for-the-badge&logo=ethernet&logoColor=000000)](https://github.com/Ringmast4r/OUI-Master-Database)
[![WiFi Mothership](https://img.shields.io/badge/WiFi_Mothership-Wardriving_Network-E5E7EB?style=for-the-badge&logo=wifi&logoColor=000000)](https://wifimothership.com/)
[![FLOCK](https://img.shields.io/badge/FLOCK-336K_Cameras-D1D5DB?style=for-the-badge&logo=cctv&logoColor=000000)](https://github.com/Ringmast4r/FLOCK)
[![Tower-Hunter](https://img.shields.io/badge/Tower--Hunter-Cell_Tower_Logger-9CA3AF?style=for-the-badge&logo=signal&logoColor=000000)](https://github.com/Ringmast4r/Tower-Hunter)

---

## `> contributing`

Issues and PRs welcome. Most-wanted contributions:

- Expand the `Combinations/` bridge beyond 813 mappings (theoretical space is 42 billion)
- Add new protocol fingerprints to `Satori_Fingerprints/` (TLS JA3/JA4, QUIC, Bluetooth)
- Country-code derivation from MAC vendor address strings
- API wrapper libraries (Go, Rust, Ruby)

---

## `> license`

Released under **MIT** — use commercially, modify, redistribute, embed in proprietary tools.

---

> *"Every day Huginn and Muninn fly over the vast earth. I fear for Huginn that he may
> not return, but I fear even more for Muninn."*
> — Odin, from the Grímnismál

*Thought is valuable. Memory is irreplaceable.*

---

**Last updated:** `2026-05-12` · **Total records:** `~11.3M` · **Maintained by** [@Ringmast4r](https://github.com/Ringmast4r)

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:6B7280,100:000000&height=120&section=footer"/>

</div>
