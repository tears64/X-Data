import requests

def run():
    print("\nTEMP MAIL")
    api = input("API URL [http://127.0.0.1:8080/api]: ").strip()
    api = api or "http://127.0.0.1:8080/api"

    print("[1] Generate address")
    print("[2] Check inbox")
    print("[3] Read message")
    print("[4] Delete inbox")
    choice = input("Select: ").strip()

    try:
        if choice == "1":
            r = requests.post(api.rstrip("/") + "/addresses", timeout=10)
            r.raise_for_status()
            print(r.json())
        elif choice == "2":
            address = input("Address: ").strip()
            r = requests.get(api.rstrip("/") + "/messages",
                             params={"address": address}, timeout=10)
            r.raise_for_status()
            print(r.json())
        elif choice == "3":
            address = input("Address: ").strip()
            message_id = input("Message ID: ").strip()
            r = requests.get(api.rstrip("/") + "/messages/" + message_id,
                             params={"address": address}, timeout=10)
            r.raise_for_status()
            print(r.json())
        elif choice == "4":
            address = input("Address: ").strip()
            r = requests.delete(api.rstrip("/") + "/addresses",
                                params={"address": address}, timeout=10)
            r.raise_for_status()
            print(r.json())
    except requests.RequestException as exc:
        print(f"Request failed: {exc}")
