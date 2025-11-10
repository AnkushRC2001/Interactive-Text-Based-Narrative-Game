# engine.py
# Core engine for "Ashes of Calcutta" text game
# Provides: typewriter printing, choice UI, state management, save/load

import sys
import time
import json
import os

# ===== CONFIG =====
TYPE_DELAY = 0.010   # seconds per character; lower = faster
PAUSE_SHORT = 0.35
PAUSE_MED = 0.9
PAUSE_LONG = 1.6
SAVE_FILE = "savegame.json"

# ===== Typewriter / print helpers =====
def typewrite(text, delay=TYPE_DELAY, newline=True):
    """Print text in typewriter style. Set delay small to speed up."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        sys.stdout.write("\n")
        sys.stdout.flush()

def p(text=""):
    typewrite(text)
    time.sleep(PAUSE_SHORT)

def pm(text=""):
    typewrite(text)
    time.sleep(PAUSE_MED)

def pl(text=""):
    typewrite(text)
    time.sleep(PAUSE_LONG)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ===== Choice UI =====
def present_choices(options):
    """Present numbered options and return chosen index (1-based)."""
    for i, opt in enumerate(options, 1):
        typewrite(f"{i}. {opt}", TYPE_DELAY / 2)
    while True:
        ans = input("\n→ Choose (number): ").strip()
        if ans.isdigit() and 1 <= int(ans) <= len(options):
            return int(ans)
        print("Invalid choice. Enter the option number.")

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
        print("Error saving state:", e)
        return False

def load_state(filename=SAVE_FILE):
    if not os.path.exists(filename):
        return default_state()
    try:
        with open(filename, "r", encoding="utf-8") as f:
            state = json.load(f)
        return state
    except Exception as e:
        print("Error loading save:", e)
        return default_state()

# ===== Inventory helpers =====
def add_item(state, item):
    if item not in state["inventory"]:
        state["inventory"].append(item)

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
    sep = "=" * 60
    print("\n" + sep)
    header = f" STATUS AFTER ACT {after_act} " if after_act else " CURRENT STATUS "
    typewrite(header)
    typewrite(f"- Morality: {state['morality']}")
    typewrite(f"- Health: {state['health']}")
    inv_display = []
    for it in state["inventory"]:
        suffix = " (used)" if state["used_items"].get(it) else ""
        inv_display.append(f"{it}{suffix}")
    typewrite("- Inventory: " + (", ".join(inv_display) if inv_display else "Empty"))
    typewrite(f"- Companion (dog): {'Buro (alive)' if state['has_dog'] else 'None'}")
    typewrite(f"- Route chosen: {state['route'] if state['route'] else 'N/A'}")
    typewrite(f"- Found Mitali: {'Yes' if state['found_mitali'] else 'No'}")
    print(sep + "\n")
    time.sleep(PAUSE_MED)


