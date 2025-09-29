from rich.console import Console
from colorama import Fore 
from rich.table import Table
from rich.align import Align
from rich.panel import Panel
import platform
import os
import tools.sys_info as sys_info
import tools.rar_cracker as rar_cracker
import tools.hash_cracker as hash_cracker
import tools.hash_builder as hash_builder
import tools.ftp_cracker as ftp_cracker
import tools.admin_finder as admin_finder
import tools.shell_cmd as shell_cmd
import tools.metasploit as metasploit
import tools.pass_cracker as pass_cracker
import tools.sqlmap as sqlmap
import tools.nmap_tool as nmap_tool
import tools.help_menu as help_menu
import tools.about as about
import tools.networktool as networktool

def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

console = Console()

# پاک‌سازی ترمینال قبل از نمایش بنر
clear_terminal()

console.print("[green]███████ ██   ██ ████████[/green] [yellow]| Launching : Shifter Toolkit[/yellow]")
console.print("[green]██      ██   ██    ██   [/green] [yellow]| Version   : 2.0.0[/yellow]")
console.print("[green]███████ ███████    ██   [/green] [yellow]| Author    : AmirHosein Sabri[/yellow]")
console.print("[green]     ██ ██   ██    ██   [/green] [yellow]| Repo      : github.com/SabriAmir/Shifter-tool[/yellow]")
console.print("[green]███████ ██   ██    ██   [/green] [yellow]| Codename  : Shifter Toolkit[/yellow]")

def menu():
    table = Table(title="[bold cyan]Shifter Toolkit[/]")
    table.add_column("Option", style="yellow", justify="center")
    table.add_column("Description", style="green")

    table.add_row("1", "System Info")
    table.add_row("2", "RAR Cracker")
    table.add_row("3", "Hash Cracker")
    table.add_row("4", "Hash Builder")
    table.add_row("5", "FTP Cracker")
    table.add_row("6", "Admin Finder")
    table.add_row("7", "Open Shell")
    table.add_row("8", "Metasploit")
    table.add_row("9", "Password Cracker")
    table.add_row("10", "SQLMap")
    table.add_row("11", "Nmap")
    table.add_row("12", "Network-tools")
    table.add_row("13", "Help Menu")
    table.add_row("14", "About")
    table.add_row("0", "Exit")

    console.print(Align.left(table, pad=1))
    

def main():
    while True:
        menu()
        print(Fore.GREEN+"  ┏━[𝚂𝚑𝚒𝚏𝚝𝚎𝚛]~[◈]")
        choice = input("  ┗━━◊")

        if choice == "1": sys_info.run()
        elif choice == "2": rar_cracker.run()
        elif choice == "3": hash_cracker.run()
        elif choice == "4": hash_builder.run()
        elif choice == "5": ftp_cracker.run()
        elif choice == "6": admin_finder.run()
        elif choice == "7": shell_cmd.run()
        elif choice == "8": metasploit.run()
        elif choice == "9": pass_cracker.run()
        elif choice == "10": sqlmap.run()
        elif choice == "11": nmap_tool.run()
        elif choice == "12": networktool.run()
        elif choice == "13": help_menu.run()
        elif choice == "14": about.run()
        elif choice == "0":
            console.print("[bold red]Exiting...[/]")
            break
        else:
            console.print("[red]Invalid option![/]")

        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()