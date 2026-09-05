import ipaddress
import requests

def locate(value):
    ip = value.strip()
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return {"type": "ip_locator", "ip": ip, "error": "Invalid IP address"}

    try:
        data = requests.get(
            f"https://ipwho.is/{ip}",
            timeout=8,
            headers={"User-Agent": "X-Data/0.8"},
        ).json()
        fields = ("continent", "country", "region", "city", "latitude",
                  "longitude", "isp", "org", "asn", "timezone")
        return {"type": "ip_locator", "ip": ip,
                **{k: data.get(k) for k in fields}}
    except Exception as exc:
        return {"type": "ip_locator", "ip": ip, "error": str(exc)}
