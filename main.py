# main.py
# Driver for "Ashes of Calcutta"
# Runs all acts sequentially with saved state continuity.

from engine import console, clear, typewrite, pm, pl
from rich.panel import Panel
import time
import sys

# Import each act's main function
import act1
import act2
import act3
import act4
import act5

def pause_between_acts():
    pl("")
    console.print("[dim]Press [Enter] to continue to the next act or type 'quit' to exit...[/dim]")
    choice = input().strip().lower()
    if choice == "quit":
        console.print("\n[yellow]Progress saved. You can resume later.[/yellow]\n")
        sys.exit(0)
    clear()

def main():
    clear()
    console.print(Panel.fit(
        "[bold white]ASHES OF CALCUTTA[/bold white]",
        subtitle="[italic]A narrative game by Ankush Roy Chowdhury[/italic]",
        style="bold red"
    ))
    pl("")

    time.sleep(1)
    console.print("[italic]Welcome back to the world of 1946 Calcutta.[/italic]\n")
    console.print("[dim]Your progress will be saved automatically between acts.[/dim]\n")
    console.print("")

    acts = [
        ("Act I — The First Fires", act1.act1_main),
        ("Act II — The Crossing", act2.act2_main),
        ("Act III — The Road to Tikiapara", act3.act3_main),
        ("Act IV — The Return", act4.act4_main),
        ("Act V — The Ashes Remember", act5.act5_main),
    ]

    for title, act_func in acts:
        clear()
        console.print(f"[bold cyan]Now playing {title}...[/bold cyan]\n")
        time.sleep(1)
        act_func()
        pause_between_acts()

    clear()
    typewrite("### THE END ###", 0.05, style="bold underline")
    pl("")
    pm("Thank you for experiencing [bold]Ashes of Calcutta[/bold].")
    pm("Created with empathy and memory — the city endures.")
    pl("")

if __name__ == "__main__":
    main()
