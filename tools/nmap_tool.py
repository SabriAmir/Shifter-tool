import os
import subprocess
from colorama import Fore

def run():
    if not os.path.exists("nmap"):
        print(Fore.YELLOW+"[!] Nmap not found, cloning from GitHub...")
        subprocess.run("git clone https://github.com/nmap/nmap.git", shell=True)
        print(Fore.GREEN+"[+] Nmap cloned successfully!")

    target = input(Fore.CYAN+"Enter target IP or hostname: ")
    try:
        print(Fore.YELLOW+"[~] Running Nmap scan...")
        subprocess.run(["nmap", "-sV", "-oN", f"nmap_report_{target}.txt", target])
        print(Fore.GREEN+f"[+] Scan completed. Report saved as nmap_report_{target}.txt")
    except Exception as e:
        print(Fore.RED+f"[!] Error running Nmap: {e}")
