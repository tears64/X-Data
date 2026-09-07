import requests

def run():
    print("\nDISCORD WEBHOOK")
    hook = input("Webhook URL: ").strip()
    message = input("Message: ").strip()
    username = input("Username (optional): ").strip()

    if not (hook.startswith("https://discord.com/api/webhooks/") or
            hook.startswith("https://discordapp.com/api/webhooks/")):
        print("Invalid Discord webhook URL.")
        return

    payload = {"content": message}
    if username:
        payload["username"] = username

    try:
        response = requests.post(hook, json=payload, timeout=10)
        print(f"HTTP status: {response.status_code}")
        print("Webhook sent." if response.ok else response.text[:300])
    except requests.RequestException as exc:
        print(f"Request failed: {exc}")
