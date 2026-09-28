from . import get_current_wifi_ssid

def cli():
    wifi_ssid = get_current_wifi_ssid()
    if wifi_ssid is not None:
        print(wifi_ssid)

cli()
