from rich.console import Console
import random

console = Console()

def run():
    password = input("Enter a numeric password to simulate cracking: ")

    console.print("[cyan]Cracking password digit by digit...[/]")
    cracked = ""
    for digit in password:
        guess = None
        while guess != digit:
            guess = str(random.randint(0, 9))
        cracked += guess
        console.print(f"[green]Cracked so far:[/] {cracked}")

    console.print(f"[bold green]Password cracked: {cracked}[/]")
