import subprocess
import platform

def get_current_wifi_ssid() -> str | None:
    os_name = platform.system()
    ssid: str | None = None
    try:
        if os_name == "Windows":
            cmd = ["netsh", "wlan", "show", "interfaces"]
            result = subprocess.run(cmd, capture_output=True, encoding="latin-1", timeout=5)
            lines = result.stdout.splitlines()
            for line in lines:
                if "SSID" in line and ":" in line:
                    _, val = line.split(":", maxsplit=1)
                    val = val.strip()
                    if val:
                        ssid = val
                        break
        elif os_name == "Darwin":
            cmd = ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"]
            result = subprocess.run(cmd, capture_output=True, encoding="latin-1", timeout=5)
            lines = result.stdout.splitlines()
            for line in lines:
                line = line.strip()
                if line.startswith(" SSID:"):
                    ssid = line.split(":", maxsplit=1)[1].strip()
                    break
        elif os_name == "Linux":
            cmd = ["iwgetid", "-r"]
            result = subprocess.run(cmd, capture_output=True, encoding="latin-1", timeout=5)
            out = result.stdout.strip()
            if out:
                ssid = out
    except Exception:
        return None
    return ssid
