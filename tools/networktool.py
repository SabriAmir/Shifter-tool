
def run():
    import socket
    import subprocess
    import threading
    from ftplib import FTP
    from getpass import getpass
    from fpdf import FPDF
    from scapy.all import sniff, TCP, UDP, ARP, Ether, srp
    from rich.console import Console
    from rich.table import Table
    from rich import box

    console = Console()
    reports = []

    # Logging helpers
    def log_info(msg): console.print(f"[bold cyan][+][/bold cyan] {msg}")
    def log_warn(msg): console.print(f"[bold yellow][!][/bold yellow] {msg}")
    def log_error(msg): console.print(f"[bold red][X][/bold red] {msg}")

    # Tools
    def port_scanner(target, ports):
        log_info(f"Scanning {target}...")
        for port in ports:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                if sock.connect_ex((target, port)) == 0:
                    log_info(f"Port {port} is open")
                    reports.append(f"[Port Scan] {target}:{port} is open")

    def sniffer(interface, filter_ip=""):
        log_info(f"Sniffing on {interface}...")
        def callback(packet):
            if TCP in packet or UDP in packet:
                src, dst = packet[0][1].src, packet[0][1].dst
                proto = "TCP" if TCP in packet else "UDP"
                if not filter_ip or src == filter_ip or dst == filter_ip:
                    console.print(f"[bold magenta]Packet:[/bold magenta] {src} → {dst} | {proto}")
                    reports.append(f"[Sniff] {src} → {dst} | {proto}")
        sniff(iface=interface, prn=callback, store=False)

    def ping_sweep(prefix):
        log_info(f"Pinging devices in {prefix}.0/24")
        for i in range(1, 255):
            ip = f"{prefix}.{i}"
            res = subprocess.run(["ping", "-n", "1", "-w", "100", ip], stdout=subprocess.DEVNULL)
            if res.returncode == 0:
                log_info(f"Host alive: {ip}")
                reports.append(f"[Ping] Host alive: {ip}")

    def ftp_brute_force(host, users, pwds):
        log_info(f"Starting FTP brute force on {host}")
        for user in users:
            for pwd in pwds:
                try:
                    ftp = FTP(host, timeout=2)
                    ftp.login(user, pwd)
                    log_info(f"Success: {user}:{pwd}")
                    reports.append(f"[FTP] Success: {user}:{pwd}")
                    ftp.quit()
                except:
                    continue

    def honeypot(port=2222):
        import socketserver
        class Handler(socketserver.BaseRequestHandler):
            def handle(self):
                ip = self.client_address[0]
                log_warn(f"Honeypot connection from {ip}")
                reports.append(f"[Honeypot] Connection from {ip}")
                self.request.send(b"Welcome to Honeypot!\n")
        server = socketserver.TCPServer(("", port), Handler)
        log_info(f"Honeypot listening on port {port}")
        server.serve_forever()

    def arp_scan(prefix):
        log_info(f"ARP scanning {prefix}.0/24")
        for i in range(1, 255):
            ip = f"{prefix}.{i}"
            pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
            resp = srp(pkt, timeout=0.5, verbose=0)[0]
            for _, r in resp:
                log_info(f"Device: {r.psrc} | MAC: {r.hwsrc}")
                reports.append(f"[ARP] {r.psrc} → {r.hwsrc}")




    def udp_scan(host, ports):
        log_info(f"UDP scan on {host}")
        for port in ports:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                try:
                    sock.sendto(b"", (host, port))
                    sock.settimeout(1)
                    sock.recvfrom(1024)
                    log_info(f"UDP {port} open")
                    reports.append(f"[UDP] {host}:{port} open")
                except:
                    continue

    def netstat_analyzer(): subprocess.call(["netstat", "-ano"])

    def wifi_scanner(): subprocess.call(["netsh", "wlan", "show", "networks", "mode=Bssid"])

    def packet_logger(interface, duration=10):
        log_info(f"Logging packets on {interface} for {duration}s")
        packets = sniff(iface=interface, timeout=duration)
        packets.summary(lambda pkt: reports.append(str(pkt)))


    def show_menu():
        table = Table(title="Network Toolkit", box=box.SIMPLE_HEAVY)
        table.add_column("Option", style="bold green", justify="center")
        table.add_column("Tool", style="bold white")
        options = [
            ("01", "Port Scanner"), ("02", "Sniffer"), ("03", "Ping Sweep"),
            ("04", "FTP Brute Force"), ("05", "Honeypot"),
            ("06", "ARP Scan"),
            ("07", "UDP Scan"),
            ("08", "Netstat Analyzer"), ("09", "Wi-Fi Network Scanner"),
            ("10", "Packet Logger"), ("0", "Exit")
        ]
        for opt, name in options:
            table.add_row(opt, name)
        console.print(table)

    def run():
        tools = {
            "1": port_scanner,
            "2": sniffer,
            "3": ping_sweep,
            "4": ftp_brute_force,
            "5": honeypot,
            "6": arp_scan,
            "7": udp_scan,
            "8": netstat_analyzer,
            "9": wifi_scanner,
            "10": packet_logger,
        }

        while True:
            show_menu()
            choice = console.input("[bold blue]Select option:[/bold blue] ").strip()
            if choice == "0":
                console.print("[bold red]Exiting... Goodbye![/bold red]")
                break
            elif choice in tools:
                try:
                    if choice in ["1"]:
                        host = console.input("Target IP: ").strip()
                        ports = list(map(int, console.input("Ports (comma separated): ").split(",")))
                        tools[choice](host, ports)
                    elif choice in ["2", "10"]:
                        iface = console.input("Interface: ").strip()
                        tools[choice](iface)
                    elif choice in ["3", "6"]:
                        prefix = console.input("Network prefix (e.g. 192.168.1): ").strip()
                        tools[choice](prefix)
                    elif choice == "4":
                        host = console.input("FTP Host: ").strip()
                        users = console.input("Usernames (comma separated): ").split(",")
                        pwds = console.input("Passwords (comma separated): ").split(",")
                        tools[choice](host, users, pwds)
                    elif choice == "7":
                        print("comeing soon...")
                    elif choice == "5":
                        port = int(console.input("Port for honeypot (default 2222): ") or "2222")
                        threading.Thread(target=tools[choice], args=(port,), daemon=True).start()
                    elif choice == "6":
                        pwd = getpass("Enter password to check: ")
                        tools[choice](pwd)
                    elif choice == "10":
                        filename = console.input("Filename (default report.pdf): ").strip() or "report.pdf"
                        tools[choice](filename)
                    elif choice == "11":
                        domain = console.input("Domain: ").strip()
                        tools[choice](domain)
                    elif choice == "14":
                        host = console.input("Target Host: ").strip()
                        tools[choice](host)
                    elif choice in ["10", "9"]:
                        tools[choice]()
                except Exception as e:
                    log_error(f"Error: {e}")
            else:
                log_warn("Invalid choice. Please try again.")

    # run menu
    run()
