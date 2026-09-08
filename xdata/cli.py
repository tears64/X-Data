from datetime import datetime
from importlib import import_module

RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"

def c(text, color):
    return f"{color}{text}{RESET}"

# Large, unmistakable X-DATA ASCII logo.
LOGO = [
    "X   X  -  DDDD   AAAAA  TTTTT  AAAAA",
    " X X   -  D   D  A   A    T    A   A",
    "  X    -  D   D  AAAAA    T    AAAAA",
    " X X   -  D   D  A   A    T    A   A",
    "X   X  -  DDDD   A   A    T    A   A",
]

TOOLS = [
    ("01", "Username Finder", "username"),
    ("02", "Email Analyzer", "email"),
    ("03", "Domain Intelligence", "domain"),
    ("04", "IP Intelligence", "ip"),
    ("05", "File Metadata", "metadata"),
    ("06", "HTTP Headers", "headers"),
    ("07", "URL Analyzer", "url"),
    ("08", "File Hash", "hash"),
    ("09", "Search Generator", "search"),
    ("10", "Port Scanner", "ports"),
    ("11", "Device Information", "device"),
    ("12", "Join Discord", None),
    ("13", "Password Generator", "password"),
    ("14", "IP Locator", "locator"),
    ("15", "Web Snapshot", "snapshot"),
    ("16", "Snap/TikTok Intel", "socialintel"),
    ("17", "OSINT Resources", "resources"),
    ("18", "Discord Webhook", "webhook"),
    ("19", "TempMail", "tempmail"),
    ("20", "Credits", "credits"),
]

SECTIONS = [
    ("OSINT", ["01","02","03","04","05"]),
    ("WEB / NETWORK", ["06","07","08","09","10","11","15"]),
    ("UTILITIES", ["13","14","16","17","19"]),
    ("COMMUNITY", ["12","18","20"]),
]

def ascii_logo():
    for i, line in enumerate(LOGO):
        color = CYAN if i < 2 else MAGENTA if i < 4 else BLUE
        print(c("  " + line, BOLD + color))
    print()
    print(c("                    X-DATA v1.2", BOLD + YELLOW))
    print(c("             PUBLIC-SOURCE OSINT TOOLKIT", WHITE))
    print(c("             " + datetime.now().strftime("%Y-%m-%d  %H:%M:%S"), BLUE))
    print()

def lookup(number):
    return next((x for x in TOOLS if x[0] == number), None)

def print_section(title, numbers):
    print(c(f"  +-- {title} " + "-" * max(0, 52-len(title)), BOLD + BLUE))
    for i in range(0, len(numbers), 2):
        left = lookup(numbers[i])
        right = lookup(numbers[i+1]) if i+1 < len(numbers) else None
        if right:
            line = f"  | [{left[0]}] {left[1]:<27} [{right[0]}] {right[1]:<27} |"
        else:
            line = f"  | [{left[0]}] {left[1]:<27}{' '*31} |"
        print(c(line, GREEN))
    print(c("  +" + "-" * 58, BLUE))

def menu():
    for title, nums in SECTIONS:
        print_section(title, nums)
    print(c("  | [00] Exit" + " " * 45 + "|", YELLOW))
    print(c("  +" + "-" * 58, BLUE))

def show_credits():
    print()
    print("  ╔══════════════════════════════════════════════════════════════╗")
    print("  ║                        X-DATA CREDITS                       ║")
    print("  ╚══════════════════════════════════════════════════════════════╝")
    print()
    print("  Made by")
    print("    elmuerte")
    print("    Discord: tears.ss")
    print()
    print("  Contributions / Support")
    print("    profane")
    print("    Discord: prfn7 / .w7mpus")
    print()
    print("  ─────────────────────────────────────────────────────────────")
    print("  Thank you for supporting X-Data.")
    print()

def main():
    while True:
        print("\033[2J\033[H", end="")
        ascii_logo()
        menu()
        choice = input("\n  X-DATA > ").strip().zfill(2)
        if choice == "00":
            print("\n  Goodbye.")
            return
        item = lookup(choice)
        if not item:
            print(c("\n  Invalid option.", YELLOW))
            input("  Press Enter...")
            continue
        _, name, module_name = item
        if module_name is None:
            print(c("\n  Discord: https://discord.gg/5qQ7q28h6", CYAN))
            input("\n  Press Enter...")
            continue
        try:
            module = import_module("xdata.modules." + module_name)
            runner = getattr(module, "run", None)
            if runner is None:
                print(c(f"\n  {name}: module entry point not found.", YELLOW))
            else:
                runner()
        except Exception as exc:
            print(c(f"\n  Error: {exc}", YELLOW))
        input("\n  Press Enter...")

if __name__ == "__main__":
    main()
