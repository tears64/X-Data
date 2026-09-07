import webbrowser

RESOURCES = [
    ("OSINT Framework", "https://osintframework.com/"),
    ("See-Know.xyz", "https://see-know.xyz/"),
    ("See-Know.ru", "https://see-know.ru/"),
    ("Temp Mail", "https://temp-mail.org/"),
    ("Have I Been Pwned", "https://haveibeenpwned.com/"),
    ("URLScan", "https://urlscan.io/"),
    ("VirusTotal", "https://www.virustotal.com/"),
    ("Shodan", "https://www.shodan.io/"),
]

def run():
    print("\nOSINT RESOURCES")
    for i, (name, url) in enumerate(RESOURCES, 1):
        print(f"[{i}] {name} - {url}")
    choice = input("\nOpen number (Enter to return): ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(RESOURCES):
        webbrowser.open(RESOURCES[int(choice) - 1][1])
