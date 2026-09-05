#!/usr/bin/env python3
import argparse
import concurrent.futures
import datetime
import os
import platform
import socket

DISCORD_URL = "https://discord.gg/5qQ7q28h6"

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    RICH = True
    console = Console()
except Exception:
    RICH = False
    console = None

MENU = {
    "1": ("username", "Username finder"),
    "2": ("email", "Email analyzer"),
    "3": ("domain", "Domain intelligence"),
    "4": ("ip", "IP intelligence"),
    "5": ("metadata", "File metadata"),
    "6": ("headers", "HTTP headers"),
    "7": ("url", "URL analyzer"),
    "8": ("hash", "File hash"),
    "9": ("search", "Search query generator"),
    "10": ("ports", "Port scanner"),
    "11": ("device", "Device information"),
    "13": ("password", "Password generator"),
    "14": ("locator", "IP locator"),
    "15": ("snapshot", "Web snapshot"),
    "16": ("socialintel", "Snap/TikTok Intel"),
}

COMMON_PORTS = {
    20:"FTP-data",21:"FTP",22:"SSH",23:"Telnet",25:"SMTP",53:"DNS",
    67:"DHCP",68:"DHCP",80:"HTTP",110:"POP3",123:"NTP",135:"MS RPC",
    139:"NetBIOS",143:"IMAP",161:"SNMP",389:"LDAP",443:"HTTPS",
    445:"SMB",465:"SMTPS",587:"SMTP submission",636:"LDAPS",
    993:"IMAPS",995:"POP3S",1433:"MSSQL",1521:"Oracle",2049:"NFS",
    3000:"HTTP-alt",3306:"MySQL",3389:"RDP",5000:"HTTP-alt",
    5432:"PostgreSQL",5900:"VNC",6379:"Redis",8000:"HTTP-alt",
    8080:"HTTP-proxy",8443:"HTTPS-alt",9200:"Elasticsearch",27017:"MongoDB"
}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def now():
    return datetime.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")

def usage():
    try:
        import psutil
        return f"{psutil.cpu_percent(interval=0.1):.0f}%", f"{psutil.virtual_memory().percent:.0f}%"
    except Exception:
        return "N/A", "N/A"

def title():
    cpu, ram = usage()
    if RICH:
        console.print("[bold cyan]" + '██╗  ██╗       ██████╗   ██████╗ ████████╗ █████╗\n╚██╗██╔╝      ██╔═══██╗ ██╔═══██╗╚══██╔══╝██╔══██╗\n ╚███╔╝ █████╗██║   ██║ ██║   ██║   ██║   ███████║\n ██╔██╗ ╚════╝██║▄▄ ██║ ██║▄▄ ██║   ██║   ██╔══██║\n██╔╝ ██╗      ╚██████╔╝ ╚██████╔╝   ██║   ██║  ██║\n╚═╝  ╚═╝       ╚══▀▀═╝   ╚══▀▀═╝    ╚═╝   ╚═╝  ╚═╝' + "[/bold cyan]")
        console.print(f"[dim]{now()}[/dim]   [bold]CPU:[/bold] {cpu}   [bold]RAM:[/bold] {ram}")
    else:
        print('██╗  ██╗       ██████╗   ██████╗ ████████╗ █████╗\n╚██╗██╔╝      ██╔═══██╗ ██╔═══██╗╚══██╔══╝██╔══██╗\n ╚███╔╝ █████╗██║   ██║ ██║   ██║   ██║   ███████║\n ██╔██╗ ╚════╝██║▄▄ ██║ ██║▄▄ ██║   ██║   ██╔══██║\n██╔╝ ██╗      ╚██████╔╝ ╚██████╔╝   ██║   ██║  ██║\n╚═╝  ╚═╝       ╚══▀▀═╝   ╚══▀▀═╝    ╚═╝   ╚═╝  ╚═╝')
        print(f"{now()}   CPU: {cpu}   RAM: {ram}")
    print()

def pretty(rows, title_text="X-Data Results"):
    if RICH:
        t = Table(title=title_text)
        if rows and isinstance(rows[0], dict):
            keys = list(rows[0])
            for k in keys: t.add_column(str(k).upper())
            for row in rows: t.add_row(*[str(row.get(k,"")) for k in keys])
        else:
            t.add_column("FIELD"); t.add_column("VALUE")
            for k,v in rows: t.add_row(str(k),str(v))
        console.print(t)
    else:
        print("\n== " + title_text + " ==")
        if rows and isinstance(rows[0], dict):
            for r in rows: print(" | ".join(f"{k}: {v}" for k,v in r.items()))
        else:
            for k,v in rows: print(f"{k}: {v}")

def device_info():
    rows = [
        ("OS", platform.system()),
        ("OS Version", platform.version()),
        ("Release", platform.release()),
        ("Architecture", platform.machine()),
        ("Hostname", socket.gethostname()),
        ("Processor", platform.processor() or "N/A"),
        ("Python", platform.python_version()),
        ("CPU Cores", os.cpu_count() or "N/A"),
    ]
    try:
        import psutil
        vm = psutil.virtual_memory()
        rows += [
            ("RAM Total", f"{vm.total/(1024**3):.2f} GB"),
            ("RAM Available", f"{vm.available/(1024**3):.2f} GB"),
            ("CPU Usage", f"{psutil.cpu_percent(interval=0.2):.0f}%"),
            ("RAM Usage", f"{vm.percent:.0f}%"),
        ]
    except Exception:
        rows.append(("Detailed RAM/CPU", "Install psutil"))
    return rows

def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.45)
    try:
        return port if s.connect_ex((host, port)) == 0 else None
    except OSError:
        return None
    finally:
        s.close()

def scan_ports(target):
    try:
        ip = socket.gethostbyname(target.strip())
    except socket.gaierror as e:
        return [("Error", str(e))]
    with concurrent.futures.ThreadPoolExecutor(max_workers=64) as pool:
        found = [p for p in pool.map(lambda p: scan_port(ip,p), sorted(COMMON_PORTS)) if p]
    if not found:
        return [{"Target":target,"Resolved IP":ip,"Open Ports":"None detected"}]
    return [{"Target":target,"Resolved IP":ip,"Port":p,"Service":COMMON_PORTS[p]} for p in found]

def run(kind, value=None):
    if kind == "ports":
        return scan_ports(value)
    if kind == "device":
        return device_info()
    if kind == "password":
        from xdata.modules.password import generate
        return generate(value or 20)
    if kind == "locator":
        from xdata.modules.locator import locate
        return locate(value)
    if kind == "snapshot":
        from xdata.snapshot import snapshot
        return snapshot(value)
    if kind == "socialintel":
        from xdata.modules.socialintel import analyze
        platform_name, username = value.split(None, 1)
        return analyze(platform_name, username)

    from xdata.modules import username, email, domain, ip, metadata, headers, url, hash as hashmod, search
    funcs = {
        "username": username.lookup,
        "email": email.lookup,
        "domain": domain.lookup,
        "ip": ip.lookup,
        "metadata": metadata.inspect,
        "headers": headers.inspect,
        "url": url.analyze,
        "hash": hashmod.compute,
        "search": search.generate,
    }
    return funcs[kind](value)

def interactive():
    while True:
        clear()
        title()
        for n, (_, label) in MENU.items():
            print(f"  [{n}] {label}")
        print("  [12] Join X-Data Discord")
        print("  [0] Exit")

        choice = input("\nX-Data > ").strip()
        if choice == "0":
            return

        if choice == "12":
            clear()
            title()
            print("X-Data Discord")
            print(DISCORD_URL)
            input("\nPress Enter...")
            continue

        if choice not in MENU:
            print("Invalid option.")
            input("Press Enter...")
            continue

        kind, label = MENU[choice]
        if kind == "password":
            value = input("Password length [20]: ").strip() or "20"
        elif kind == "socialintel":
            platform_name = input("Platform (Snapchat/TikTok): ").strip()
            username = input("Username: ").strip()
            value = f"{platform_name} {username}"
        elif kind == "snapshot":
            value = input("URL (authorized site): ").strip()
        else:
            prompt = "Target" if kind in ("ports", "locator") else label
            value = input(prompt + ": ").strip()

        clear()
        title()
        try:
            result = run(kind, value)
            if isinstance(result, dict):
                result = list(result.items())
            if isinstance(result, list):
                pretty(result, label)
            else:
                print(result)
        except Exception as exc:
            print("[!] Error:", exc)
        input("\nPress Enter to return to menu...")

def main():
    p = argparse.ArgumentParser(prog="xdata")
    p.add_argument("--menu", action="store_true")
    sub = p.add_subparsers(dest="command")
    for name in ["username","email","domain","ip","metadata","headers","url","hash","search"]:
        q=sub.add_parser(name); q.add_argument("value")
    q=sub.add_parser("ports", aliases=["portscan"]); q.add_argument("target")
    q=sub.add_parser("password"); q.add_argument("length", nargs="?", default="20")
    q=sub.add_parser("locator", aliases=["ip-locate"]); q.add_argument("ip")
    q=sub.add_parser("snapshot", aliases=["web-snapshot"]); q.add_argument("url")
    q=sub.add_parser("socialintel", aliases=["snapintel"]); q.add_argument("platform"); q.add_argument("username")
    sub.add_parser("device", aliases=["device-info","sysinfo"])
    a=p.parse_args()
    if a.command is None or a.menu:
        interactive(); return
    kind = ("ports" if a.command in ("ports", "portscan") else
            "device" if a.command in ("device", "device-info", "sysinfo") else
            "locator" if a.command in ("locator", "ip-locate") else
            "snapshot" if a.command in ("snapshot", "web-snapshot") else
            "socialintel" if a.command in ("socialintel", "snapintel") else
            a.command)
    if kind == "socialintel":
        value = f"{a.platform} {a.username}"
    elif kind == "password":
        value = a.length
    else:
        value = getattr(a, "target", None) or getattr(a, "url", None) or getattr(a, "ip", None) or getattr(a, "value", None)
    result = run(kind, value)
    if isinstance(result,dict): result=list(result.items())
    if isinstance(result,list): pretty(result, kind.title())
    else: print(result)

if __name__ == "__main__":
    main()
