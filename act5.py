# act5.py
# Act V — The Ashes Remember (final act, moral climax, epilogues)
# Requires engine.py and prior saves.

from engine import *

def act5_main():
    state = load_state()
    state['act'] = 5
    clear()
    typewrite("# ASHES OF CALCUTTA", 0.02)
    pm("ACT V — THE ASHES REMEMBER")
    pm("(Rajendra Deb Lane / Thanthania Kali Bari — Morning after reunion)")
    pl("")

    p("Scene 1 — Morning After")
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
        else:
            p("You tuck the tin away and go into the lane to find more.")
    else:
        p("You have nothing. Hunger tugs at your ribs as you go.")

    # Alley encounter
    pl("\nScene 2 — The Alley of Hunger")
    p("Behind a ruined spice shop, the dog stops and whines. A boy emerges from the shadow — no more than sixteen, clothes torn, eyes ringed with soot. In his hand a sharpened scrap gleams.")
    p("'Leave the food. I won't ask twice,' he says.")
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
    elif chosen.startswith("Defend bare-handed"):
        state['health'] = max(0, state['health'] - 1)
        p("You grapple, mud and rain in your face. You wrench the blade away but feel the sting of a cut. (health -1)")
    elif chosen.startswith("Let Buro"):
        p("Buro leaps and pins the boy with a low growl. Mitali whispers 'Good boy...' The boy trembles.")
    else:
        p("You speak of children and hunger. His fingers loosen; tears fall and he kneels in the mud.")

    p("He pleads: 'Please… I have no one. Don't kill me.'")
    final = present_choices(["Spare the boy — let him go with food", "Kill the boy — end the threat"])
    if final == 1:
        state['morality'] += 3
        p("You drop the weapon. 'Go,' you say. 'Take what you need. Don't come back with blood in your hands.' The boy grabs rice and runs. Mitali holds your hand.")
        epilogue_forgiveness(state)
    else:
        state['morality'] -= 5
        p("Your hand moves before thought. The blow is quick and the boy's cry is small and sudden. Rain mixes with blood. Mitali screams. The silence after is a wound.")
        epilogue_vendetta(state)

    save_state(state)
    show_status(state, after_act=5)

def epilogue_forgiveness(state):
    pl("\nEPILOGUE — Forgiveness")
    p("At Thanthania Kali Bari the temple lamps burn low. Neighbors exchange rations and children learn to laugh again. The dog sleeps at Mitali's feet.")
    p("You help board a sagging door. The work is small, but each hammered nail stitches the lane back together.")
    p("You whisper a prayer: 'We will remember, and we will rebuild.'")
    p("A quiet begins to grow where chaos was.")

def epilogue_vendetta(state):
    pl("\nEPILOGUE — Consequence")
    p("You return to your house hollow with a silence that will not lift. The knife lies on the floor, an accusation you cannot wash away.")
    p("Neighbors look away; their meals are smaller; the lane is quieter. Mitali sleeps but wakes with dreams the way children do after storms. The price of the final blow is paid in small, silent ways every day.")

if __name__ == "__main__":
    act5_main()
