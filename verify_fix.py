
import sys
from engine import present_choices, quick_time_event, console

def verify():
    console.print("[bold]Verifying Fix...[/bold]")
    
    # Test 1: Choices
    console.print("\n[cyan]Test 1: Present Choices[/cyan]")
    console.print("Expected: Should show numbered list and ask for input (since we are non-interactive)")
    
    # Mock input to avoid blocking indefinitely if it works
    # We can't easily mock input() in a subprocess without pipe interaction, 
    # but for this environment, I can just run it and see if it crashes or prompts.
    # Actually, if I run this via run_command, I can send input!
    
    try:
        # We will need to send "1\n" to this process
        choice = present_choices(["Option A", "Option B"])
        console.print(f"Selected Index: {choice}")
    except Exception as e:
        console.print(f"[red]FAILED: {e}[/red]")
        import traceback
        traceback.print_exc()

    # Test 2: QTE
    console.print("\n[cyan]Test 2: Quick Time Event[/cyan]")
    console.print("Expected: Should auto-succeed in non-interactive mode")
    result = quick_time_event("TEST QTE", 2.0, lambda: print("Success!"), lambda: print("Fail!"))
    console.print(f"QTE Result: {result}")

if __name__ == "__main__":
    verify()
