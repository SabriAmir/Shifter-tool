import platform
from rich.console import Console
from rich.table import Table

console = Console()

def run():
    console.print("[bold cyan]System Information[/]\n")

    table = Table(title="System Info")
    table.add_column("Property", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("System", platform.system())
    table.add_row("Node Name", platform.node())
    table.add_row("Release", platform.release())
    table.add_row("Version", platform.version())
    table.add_row("Machine", platform.machine())
    table.add_row("Processor", platform.processor())

    console.print(table)
