# get-current-wifi-ssid
Get SSID of the current WIFI connection.

## Installation
```bash
pip install get-current-wifi-ssid
```

## Usage

### CLI

```bash
# Output the ssid if wifi is connected
# Output nothing if no wifi is connected
python -m get_current_wifi_ssid
```

### Python API

```python
from get_current_wifi_ssid import get_current_wifi_ssid

wifi_ssid = get_current_wifi_ssid()
if wifi_ssid is None:
    print("No wifi is connected.")
else:
    print("Current wifi ssid is [%s]" % wifi_ssid)
```
