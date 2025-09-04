import os
import subprocess
from colorama import Fore

def run():
    if not os.path.exists("sqlmap"):
        print(Fore.YELLOW+"[!] SQLMap not found, cloning from GitHub...")
        subprocess.run("git clone https://github.com/sqlmapproject/sqlmap.git", shell=True)
        print(Fore.GREEN+"[+] SQLMap cloned successfully!")

    target = input(Fore.CYAN+"Enter target URL (e.g., http://testphp.vulnweb.com/listproducts.php?cat=1): ")
    try:
        print(Fore.YELLOW+"[~] Running SQLMap...")
        subprocess.run(["python3", "sqlmap/sqlmap.py", "-u", target, "--batch", "--output-dir=reports"])
        print(Fore.GREEN+"[+] SQLMap finished! Reports saved in 'reports/'")
    except Exception as e:
        print(Fore.RED+f"[!] Error running SQLMap: {e}")
