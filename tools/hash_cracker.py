import hashlib
from rich.console import Console

console = Console()

def run():
    target_hash = input("Enter hash (SHA1): ")
    wordlist = input("Enter path to wordlist: ")

    try:
        with open(wordlist, "r") as f:
            passwords = f.read().splitlines()
    except FileNotFoundError:
        console.print("[red]Wordlist file not found![/]")
        return

    for password in passwords:
        hash_try = hashlib.sha1(password.encode()).hexdigest()
        if hash_try == target_hash:
            console.print(f"[green]Password found:[/] {password}")
            return
        else:
            console.print(f"[yellow]Trying:[/] {password}")

    console.print("[red]Password not found.[/]")
