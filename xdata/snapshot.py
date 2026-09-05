from pathlib import Path
from urllib.parse import urljoin, urlparse
import re
import requests

def snapshot(url, output_dir="xdata_snapshot"):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    out = Path(output_dir).expanduser()
    out.mkdir(parents=True, exist_ok=True)

    r = requests.get(
        url, timeout=12,
        headers={"User-Agent": "X-Data/0.8"},
        allow_redirects=True,
    )
    r.raise_for_status()
    html = r.text
    source = urlparse(r.url)
    saved = 0

    refs = re.findall(r'''(?:src|href)=["']([^"']+)["']''', html, re.I)
    extensions = (".css", ".js", ".png", ".jpg", ".jpeg", ".gif",
                  ".svg", ".webp", ".ico", ".woff", ".woff2", ".ttf", ".otf")

    for ref in refs:
        if ref.startswith(("data:", "javascript:", "#", "mailto:", "tel:")):
            continue
        asset = urljoin(r.url, ref)
        parsed = urlparse(asset)
        if parsed.netloc and parsed.netloc != source.netloc:
            continue
        if not parsed.path.lower().endswith(extensions):
            continue
        try:
            a = requests.get(asset, timeout=8,
                             headers={"User-Agent": "X-Data/0.8"})
            if a.ok:
                name = Path(parsed.path).name or f"asset_{saved}"
                (out / name).write_bytes(a.content)
                saved += 1
        except requests.RequestException:
            pass

    (out / "index.html").write_text(html, encoding="utf-8")
    return {
        "type": "web_snapshot",
        "source_url": r.url,
        "output_directory": str(out.resolve()),
        "assets_saved": saved,
        "note": "Use only for sites you own or are authorized to archive. No cookies, logins, forms, or credentials are copied.",
    }
