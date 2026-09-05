import socket
import requests
import dns.resolver

def run(value):
    domain = value.strip().lower().rstrip(".")
    result = {"type": "domain", "domain": domain, "dns": {}, "rdap": None}

    for record in ("A", "AAAA", "MX", "NS", "TXT"):
        try:
            answers = dns.resolver.resolve(domain, record, lifetime=5)
            result["dns"][record] = [a.to_text() for a in answers]
        except Exception:
            result["dns"][record] = []

    try:
        result["rdap"] = requests.get(
            f"https://rdap.org/domain/{domain}",
            timeout=8,
            headers={"User-Agent": "X-Data/0.2"},
        ).json()
    except Exception as exc:
        result["rdap"] = {"error": str(exc)}

    return result


# Compatibility entry point used by the X-Data CLI.
def lookup(value):
    return run(value)
