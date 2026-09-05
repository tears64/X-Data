from urllib.parse import urlparse, parse_qs

def run(value):
    raw = value.strip()
    parsed = urlparse(raw if "://" in raw else "https://" + raw)
    return {
        "type": "url",
        "url": raw,
        "scheme": parsed.scheme,
        "hostname": parsed.hostname,
        "port": parsed.port,
        "path": parsed.path,
        "query_parameters": {k: v for k, v in parse_qs(parsed.query).items()},
        "fragment_present": bool(parsed.fragment),
    }


# Compatibility entry point used by the X-Data CLI.
def analyze(value):
    return run(value)
