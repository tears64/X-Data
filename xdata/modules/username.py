from ..http import get

# Public profile URL templates. Providers are intentionally limited to
# public profile pages and ordinary HTTP status checks.
SITES = {
    "GitHub": "https://github.com/{u}",
    "Reddit": "https://www.reddit.com/user/{u}/",
    "GitLab": "https://gitlab.com/{u}",
    "Codeberg": "https://codeberg.org/{u}",
    "TikTok": "https://www.tiktok.com/@{u}",
    "Snapchat": "https://www.snapchat.com/add/{u}",
    "Pinterest": "https://www.pinterest.com/{u}/",
    "Twitch": "https://www.twitch.tv/{u}",
    "Telegram": "https://t.me/{u}",
    "Keybase": "https://keybase.io/{u}",
}

def run(value):
    u = value.strip().lstrip("@")
    results = []
    for site, template in SITES.items():
        url = template.format(u=u)
        try:
            r = get(url)
            exists = r.status_code == 200
            results.append({
                "site": site,
                "url": url,
                "status_code": r.status_code,
                "exists": exists,
            })
        except Exception as exc:
            results.append({
                "site": site,
                "url": url,
                "status_code": None,
                "exists": None,
                "error": str(exc),
            })
    return {"type": "username", "username": u, "results": results}


# Compatibility entry point used by the X-Data CLI.
def lookup(username):
    return run(username)
