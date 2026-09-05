from ..http import get

def run(value):
    url = value.strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    r = get(url)
    return {
        "type": "headers",
        "url": url,
        "status": r.status_code,
        "final_url": r.url,
        "server": r.headers.get("Server"),
        "content_type": r.headers.get("Content-Type"),
        "headers": dict(r.headers),
    }


# Compatibility entry point used by the X-Data CLI.
def inspect(value):
    return run(value)
