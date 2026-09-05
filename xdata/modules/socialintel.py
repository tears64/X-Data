from ..http import get

def analyze(platform, username):
    p = platform.strip().lower()
    site = "Snapchat" if p in ("snap", "snapchat") else "TikTok" if p == "tiktok" else None
    if not site:
        return {"type": "socialintel", "error": "Use Snapchat or TikTok"}

    user = username.strip().lstrip("@")
    url = f"https://www.snapchat.com/add/{user}" if site == "Snapchat" else f"https://www.tiktok.com/@{user}"
    try:
        r = get(url)
        return {
            "type": "socialintel",
            "platform": site,
            "username": user,
            "profile_url": url,
            "status_code": r.status_code,
            "public_profile_reachable": r.status_code == 200,
            "note": "Public URL status is not proof of identity or account ownership.",
        }
    except Exception as exc:
        return {"type": "socialintel", "platform": site, "username": user,
                "profile_url": url, "error": str(exc)}
