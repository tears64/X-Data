import requests

UA = "X-Data/0.2 (+public-osint)"

def get(url, timeout=8):
    return requests.get(
        url,
        timeout=timeout,
        headers={"User-Agent": UA},
        allow_redirects=True,
    )
