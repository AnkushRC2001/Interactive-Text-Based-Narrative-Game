
import sys
import questionary
from rich.console import Console

console = Console()

def test_questionary():
    print(f"Is TTY: {sys.stdout.isatty()}")
    try:
        choice = questionary.select(
            "Test Choice:",
            choices=["Option 1", "Option 2"]
        ).ask()
        print(f"Selected: {choice}")
    except Exception as e:
        print(f"Questionary failed: {e}")
        # Print traceback to see if it matches
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_questionary()
