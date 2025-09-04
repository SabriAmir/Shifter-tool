import rarfile
import time
from rich.console import Console

console = Console()

def run():
    rarfile_address = input("Enter path to RAR file: ")
    wordlist = input("Enter path to wordlist: ")

    try:
        rf = rarfile.RarFile(rarfile_address)
    except Exception as e:
        console.print(f"[red]Error opening file:[/] {e}")
        return

    try:
        with open(wordlist, "r") as f:
            passwords = f.read().splitlines()
    except FileNotFoundError:
        console.print("[red]Wordlist file not found![/]")
        return

    start = time.time()
    for password in passwords:
        try:
            rf.extractall(pwd=password.encode())
            end = time.time()
            console.print(f"[green]Success! Password:[/] {password} in {end-start:.2f}s")
            return
        except:
            console.print(f"[yellow]Failed:[/] {password}")

    console.print("[red]Password not found in wordlist.[/]")
