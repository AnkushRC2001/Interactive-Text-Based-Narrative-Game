# main.py
# Driver for "Ashes of Calcutta"
# Runs all acts sequentially with saved state continuity.

from engine import clear, typewrite, pm, pl
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
    choice = input("Press [Enter] to continue to the next act or type 'quit' to exit: ").strip().lower()
    if choice == "quit":
        print("\nProgress saved. You can resume later.\n")
        sys.exit(0)
    clear()

def main():
    clear()
    typewrite("# ASHES OF CALCUTTA", 0.03)
    pm("A narrative game by Ankush Roy Chowdhury")
    pm("------------------------------------------------")
    pl("")

    time.sleep(1)
    print("Welcome back to the world of 1946 Calcutta.\n")
    print("Your progress will be saved automatically between acts.\n")
    print("")

    acts = [
        ("Act I — The First Fires", act1.act1_main),
        ("Act II — The Crossing", act2.act2_main),
        ("Act III — The Road to Tikiapara", act3.act3_main),
        ("Act IV — The Return", act4.act4_main),
        ("Act V — The Ashes Remember", act5.act5_main),
    ]

    for title, act_func in acts:
        clear()
        print(f"Now playing {title}...\n")
        time.sleep(1)
        act_func()
        pause_between_acts()

    clear()
    typewrite("### THE END ###", 0.05)
    pl("")
    pm("Thank you for experiencing *Ashes of Calcutta*.")
    pm("Created with empathy and memory — the city endures.")
    pl("")

if __name__ == "__main__":
    main()
