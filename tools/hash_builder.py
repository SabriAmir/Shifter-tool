import hashlib
from rich.console import Console

console = Console()

def run():
    text = input("Enter text to hash: ")
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    sha1_hash = hashlib.sha1(text.encode()).hexdigest()

    console.print(f"[cyan]MD5:[/] {md5_hash}")
    console.print(f"[cyan]SHA1:[/] {sha1_hash}")
