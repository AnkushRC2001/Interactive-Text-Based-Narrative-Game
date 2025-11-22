# engine.py
# Core engine for "Ashes of Calcutta" text game
# Provides: typewriter printing, choice UI, state management, save/load
# Updated for Telltale-style visuals using 'rich' and 'questionary'

import sys
import time
import json
import os
import msvcrt  # For QTEs on Windows

from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.table import Table
from rich.style import Style
from rich.theme import Theme
import questionary

# ===== CONFIG =====
TYPE_DELAY = 0.010   # seconds per character; lower = faster
PAUSE_SHORT = 0.35
PAUSE_MED = 0.9
PAUSE_LONG = 1.6
SAVE_FILE = "savegame.json"

# Custom Theme
custom_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red",
    "success": "bold green",
    "narrative": "white",
    "choice": "yellow",
    "notification": "bold italic cyan"
})

console = Console(theme=custom_theme)

# ===== Typewriter / print helpers =====
def typewrite(text, delay=TYPE_DELAY, style=None, newline=True):
    """Print text in typewriter style with rich formatting."""
    # If text has rich markup, we need to handle it carefully for typewriter effect.
    # For simplicity in this version, we'll use rich's print for styled text 
    # but simulate typewriter by printing chunks or just printing directly if it's complex.
    # A true rich typewriter is complex, so we'll stick to a simple char-by-char for plain text
    # and direct print for complex markup to avoid breaking tags.
    
    if "[" in text and "]" in text:
        # Has markup, print directly to avoid breaking tags during iteration
        # Or we could use console.print with a live display, but that's advanced.
        # Let's just print it with a small delay before to simulate 'thinking'.
        time.sleep(delay * 10)
        console.print(text, style=style, end="\n" if newline else "")
    else:
        # Plain text, do the typewriter effect
        for ch in text:
            console.print(ch, style=style, end="")
            time.sleep(delay)
        if newline:
            console.print()

def p(text="", style="narrative"):
    typewrite(text, style=style)
    time.sleep(PAUSE_SHORT)

def pm(text="", style="narrative"):
    typewrite(text, style=style)
    time.sleep(PAUSE_MED)

def pl(text="", style="narrative"):
    typewrite(text, style=style)
    time.sleep(PAUSE_LONG)

def clear():
    console.clear()

def notify(text, style="notification"):
    """Displays a Telltale-style notification."""
    console.print()
    console.print(Panel(text, style=style, expand=False))
    time.sleep(PAUSE_MED)

# ===== Choice UI =====
def present_choices(options):
    """Present options using questionary (arrow keys) and return chosen index (1-based)."""
    # options is a list of strings.
    # questionary.select returns the string chosen.
    choice = questionary.select(
        "Make your choice:",
        choices=options,
        style=questionary.Style([
            ('qmark', 'fg:#E91E63 bold'),       # token in front of the question
            ('question', 'bold'),               # question text
            ('answer', 'fg:#2196f3 bold'),      # submitted answer text
            ('pointer', 'fg:#673ab7 bold'),     # pointer used in select and checkbox
            ('highlighted', 'fg:#673ab7 bold'), # pointed-at choice in select and checkbox
            ('selected', 'fg:#cc5454'),         # selected choice in checkbox
            ('separator', 'fg:#cc5454'),        # separator in select
            ('instruction', ''),                # user instructions for select, rawselect, checkbox
            ('text', ''),                       # plain text
            ('disabled', 'fg:#858585 italic')   # disabled choices for select, rawselect, checkbox
        ])
    ).ask()
    
    # Find index
    return options.index(choice) + 1

def quick_time_event(prompt, timeout, success_action, fail_action):
    """
    Waits for ANY key press within 'timeout' seconds.
    Returns True if successful, False otherwise.
    """
    console.print(f"\n[bold red]!!! {prompt} !!![/bold red]")
    console.print(f"[dim]Press any key within {timeout} seconds![/dim]")
    
    start_time = time.time()
    # Flush input buffer
    while msvcrt.kbhit():
        msvcrt.getch()
        
    while time.time() - start_time < timeout:
        if msvcrt.kbhit():
            msvcrt.getch() # Consume key
            success_action()
            return True
        time.sleep(0.05)
    
    fail_action()
    return False

# ===== Game State =====
def default_state():
    return {
        "act": 1,
        "morality": 0,
        "health": 10,
        "inventory": [],         # list of strings
        "used_items": {},        # item -> True if consumed
        "has_dog": False,
        "route": None,           # 'river'/'ground'/'bridge'
        "found_mitali": False,
        "safe_route_unlocked": False,
        "directions_to_nimtala": False
    }

def save_state(state, filename=SAVE_FILE):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        console.print(f"[bold red]Error saving state: {e}[/bold red]")
        return False

def load_state(filename=SAVE_FILE):
    if not os.path.exists(filename):
        return default_state()
    try:
        with open(filename, "r", encoding="utf-8") as f:
            state = json.load(f)
        return state
    except Exception as e:
        console.print(f"[bold red]Error loading save: {e}[/bold red]")
        return default_state()

# ===== Inventory helpers =====
def add_item(state, item):
    if item not in state["inventory"]:
        state["inventory"].append(item)
        notify(f"Item Added: {item}", style="success")

def has_item(state, item):
    return item in state["inventory"] and not state["used_items"].get(item, False)

def use_item(state, item):
    if item in state["inventory"] and not state["used_items"].get(item, False):
        state["used_items"][item] = True
        return True
    return False

def remove_item(state, item):
    if item in state["inventory"]:
        state["inventory"].remove(item)
    if item in state["used_items"]:
        del state["used_items"][item]

# ===== Status display =====
def show_status(state, after_act=None):
    console.print()
    
    title = f"STATUS AFTER ACT {after_act}" if after_act else "CURRENT STATUS"
    
    table = Table(title=title, show_header=False, box=None)
    table.add_column("Key", style="dim cyan")
    table.add_column("Value", style="white")
    
    table.add_row("Morality", str(state['morality']))
    table.add_row("Health", str(state['health']))
    
    inv_display = []
    for it in state["inventory"]:
        suffix = " (used)" if state["used_items"].get(it) else ""
        inv_display.append(f"{it}{suffix}")
    
    table.add_row("Inventory", ", ".join(inv_display) if inv_display else "Empty")
    table.add_row("Companion", "Buro (alive)" if state['has_dog'] else "None")
    table.add_row("Route", state['route'] if state['route'] else "N/A")
    table.add_row("Found Mitali", "Yes" if state['found_mitali'] else "No")
    
    console.print(Panel(table, expand=False))
    time.sleep(PAUSE_MED)


