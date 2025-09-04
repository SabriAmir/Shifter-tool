import os
from rich.console import Console

console = Console()

def run():
    console.print("[cyan]Opening system shell...[/]")
    os.system("cmd" if os.name == "nt" else "bash")
