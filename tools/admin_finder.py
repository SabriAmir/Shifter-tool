import requests
from rich.console import Console

console = Console()

def run():
    website = input("Enter website (e.g. http://example.com): ")
    wordlist = input("Enter path to URL list: ")

    try:
        with open(wordlist, "r") as f:
            paths = f.read().splitlines()
    except FileNotFoundError:
        console.print("[red]URL list not found![/]")
        return

    for path in paths:
        url = f"{website}/{path}"
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                console.print(f"[green]Found:[/] {url}")
            else:
                console.print(f"[yellow]Not found:[/] {url}")
        except Exception as e:
            console.print(f"[red]Error:[/] {e}")
