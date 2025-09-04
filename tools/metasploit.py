import os
import subprocess
from colorama import Fore

def run():
    if not os.path.exists("metasploit-framework"):
        print(Fore.YELLOW+"[!] Metasploit not found, cloning from GitHub...")
        subprocess.run("git clone https://github.com/rapid7/metasploit-framework.git", shell=True)
        print(Fore.GREEN+"[+] Metasploit cloned successfully!")

    try:
        print(Fore.CYAN+"[~] Starting Metasploit...")
        subprocess.run(["msfconsole"])
    except Exception as e:
        print(Fore.RED+f"[!] Error running Metasploit: {e}")
