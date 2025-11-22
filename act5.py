# act5.py
# Act V — The Ashes Remember (final act, moral climax, epilogues)
# Requires engine.py and prior saves.

from engine import *

def act5_main():
    state = load_state()
    state['act'] = 5
    clear()
    typewrite("# ASHES OF CALCUTTA", 0.02, style="bold underline")
    pm("ACT V — THE ASHES REMEMBER", style="bold")
    pm("(Rajendra Deb Lane / Thanthania Kali Bari — Morning after reunion)", style="dim italic")
    pl("")

    p("Scene 1 — Morning After", style="bold")
    p("The house has holes where the roof once kept out rain. Mitali sleeps beside you, wrapped in a shawl faint with smoke. The dog lies by the door, lifted ear hearing each small sound.")
    if has_item(state, "whistle"):
        p("The dented whistle rests in a pocket — a memory of the constable's last breath.")
    if has_item(state, "rusty_knife"):
        p("The rusty knife lies nearby — dull, a dark comfort.")
    if has_item(state, "biscuits"):
        p("A half-tin of biscuits offers a small mercy.")

    p("Mitali tugs your sleeve: 'Baba, we have no food left.' You step into Rajendra Deb Lane. The scent of ash and burnt ghee lingers.")
    if has_item(state, "biscuits"):
        c = present_choices(["Give the biscuits to Mitali now", "Save the biscuits and search the lane"])
        if c == 1:
            use_item(state, "biscuits")
            p("You break the tin and give biscuits to Mitali. She eats slowly, eyes brightening.")
            notify("Mitali is grateful", style="success")
        else:
            p("You tuck the tin away and go into the lane to find more.")
            notify("Mitali is hungry", style="warning")
    else:
        p("You have nothing. Hunger tugs at your ribs as you go.")

    # Alley encounter
    pl("\nScene 2 — The Alley of Hunger", style="bold")
    p("Behind a ruined spice shop, the dog stops and whines. A boy emerges from the shadow — no more than sixteen, clothes torn, eyes ringed with soot. In his hand a sharpened scrap gleams.")
    p("'Leave the food. I won't ask twice,' he says.", style="warning")
    
    opts = []
    if has_item(state, "rusty_knife"):
        opts.append("Defend with the rusty knife (disarm)")
    else:
        opts.append("Defend bare-handed (grapple and disarm)")
    if state['has_dog']:
        opts.append("Let Buro intervene")
    opts.append("Try to reason with the boy")
    
    ch = present_choices(opts)
    chosen = opts[ch-1]
    
    if chosen.startswith("Defend with the rusty knife"):
        p("Steel flashes. You twist and the boy's weapon skitters across the cobbles. He falls back, clutching his arm.")
        notify("Disarmed Enemy", style="success")
    elif chosen.startswith("Defend bare-handed"):
        p("You lunge at him!")
        # QTE
        if quick_time_event("GRAPPLE", 1.5, lambda: None, lambda: None):
            p("You catch his wrist and twist it. The blade clatters to the ground.", style="success")
        else:
            state['health'] = max(0, state['health'] - 1)
            p("You grapple, mud and rain in your face. You wrench the blade away but feel the sting of a cut.", style="danger")
            notify("Health -1", style="danger")
    elif chosen.startswith("Let Buro"):
        p("Buro leaps and pins the boy with a low growl. Mitali whispers 'Good boy...' The boy trembles.")
        notify("Buro protected you", style="success")
    else:
        p("You speak of children and hunger. His fingers loosen; tears fall and he kneels in the mud.")
        notify("Reasoned with Enemy", style="success")

    p("He pleads: 'Please… I have no one. Don't kill me.'", style="italic")
    
    # Dramatic final choice
    console.print(Panel("[bold red]FINAL DECISION[/bold red]", style="bold red"))
    final = present_choices(["Spare the boy — let him go with food", "Kill the boy — end the threat"])
    
    if final == 1:
        state['morality'] += 3
        p("You drop the weapon. 'Go,' you say. 'Take what you need. Don't come back with blood in your hands.' The boy grabs rice and runs. Mitali holds your hand.")
        notify("Morality +3", style="success")
        notify("Mitali will remember your mercy.", style="info")
        epilogue_forgiveness(state)
    else:
        state['morality'] -= 5
        p("Your hand moves before thought. The blow is quick and the boy's cry is small and sudden. Rain mixes with blood. Mitali screams. The silence after is a wound.", style="bold red")
        notify("Morality -5", style="danger")
        notify("Mitali will remember your violence.", style="danger")
        epilogue_vendetta(state)

    save_state(state)
    show_status(state, after_act=5)

def epilogue_forgiveness(state):
    pl("\nEPILOGUE — Forgiveness", style="bold green")
    p("At Thanthania Kali Bari the temple lamps burn low. Neighbors exchange rations and children learn to laugh again. The dog sleeps at Mitali's feet.")
    p("You help board a sagging door. The work is small, but each hammered nail stitches the lane back together.")
    p("You whisper a prayer: 'We will remember, and we will rebuild.'")
    p("A quiet begins to grow where chaos was.")

def epilogue_vendetta(state):
    pl("\nEPILOGUE — Consequence", style="bold red")
    p("You return to your house hollow with a silence that will not lift. The knife lies on the floor, an accusation you cannot wash away.")
    p("Neighbors look away; their meals are smaller; the lane is quieter. Mitali sleeps but wakes with dreams the way children do after storms. The price of the final blow is paid in small, silent ways every day.")

if __name__ == "__main__":
    act5_main()
