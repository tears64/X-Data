import ipaddress
import socket
import requests

def run(value):
    ip = str(ipaddress.ip_address(value.strip()))
    result = {"type": "ip", "ip": ip, "reverse_dns": None, "rdap": None}

    try:
        result["reverse_dns"] = socket.gethostbyaddr(ip)[0]
    except Exception:
        result["reverse_dns"] = None

    try:
        result["rdap"] = requests.get(
            f"https://rdap.org/ip/{ip}",
            timeout=8,
            headers={"User-Agent": "X-Data/0.2"},
        ).json()
    except Exception as exc:
        result["rdap"] = {"error": str(exc)}

    return result


# Compatibility entry point used by the X-Data CLI.
def lookup(value):
    return run(value)
