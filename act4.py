# act4.py
# Act IV — The Return (Howrah → Calcutta, reunion)
# Requires engine.py and prior saves.

from engine import *

def act4_main():
    state = load_state()
    state['act'] = 4
    clear()
    typewrite("# ASHES OF CALCUTTA", 0.02)
    pm("ACT IV — THE RETURN")
    pm("(Howrah to Calcutta — Evening)")
    pl("")

    p("Scene 1 — Crossing Decision")
    p("The river is a black mirror; both banks glow where fires lick at roofs. The Howrah Bridge looms through smoke, its metal ribs swallowed by haze.")
    p("You must cross — the bridge or the river. One will take you to Burrabazar and Harrison Road; the other will land you at Mullick Ghat and Strand Road.")
    c = present_choices(["Cross by Howrah Bridge", "Cross by boat via Mullick Ghat"])
    if c == 1:
        state['route'] = "bridge"
        state['health'] -= 1
        p("You join the crowd beneath the lattice. Gunfire cracks. You push through smoke and bodies until you stumble into Burrabazar. (health -1)")
    else:
        state['route'] = "river"
        if has_item(state, "silver_locket"):
            use_item(state, "silver_locket")
            p("You offer the silver locket. The boatman accepts it with reverence and rows you across. (locket used)")
        else:
            p("You beg the boatman with empty hands and a tremor in your voice. He takes pity and rows you across.")
        p("The river moves like thick ink and Strand Road burns in reflected light.")

    # Scene 2 — Mullick Ghat / Strand Road or view from bridge
    pl("\nScene 2 — Approaching Burrabazar")
    if state['route'] == "river":
        p("Mullick Ghat (flower market) lies in ruin — marigolds crushed into the mud, baskets broken, incense damp. Strand Road's warehouses gape like wounds.")
        if state['has_dog']:
            p("Buro's nose leads you past a gang of looters behind a cart; you avoid an ambush.")
        else:
            p("You stumble over debris and feel the city press at you like a closing hand.")
    else:
        p("From the bridge you see both shores burning, people running like shadows, roofs collapsing into sparks. The sight makes your stomach drop and your breath short.")

    p("Burrabazar is a ruined maze of spice and cloth stalls. Harrison Road cuts through smoke and charred awnings.")
    p("A man rushes from a doorway with a knife; his eyes are raw with fear.")
    if state['has_dog']:
        p("Buro leaps forward, barking. The man falters and lowers the blade. 'Go, dada. Go before they come again.'")
    else:
        if has_item(state, "rusty_knife"):
            p("You show the rusty knife; faces part and you pass, hands trembling.")
        else:
            state['health'] -= 2
            p("A scuffle leaves you bleeding and breathless. (health -2)")

    # Scene 3 — Rajendra Deb Lane & Reunion
    pl("\nScene 3 — Rajendra Deb Lane")
    p("You turn into your lane. The house door hangs open. Inside soot coats everything; the ceiling fan droops like a wilted flower.")
    p("'Mitali? Baba aschhe' you whisper, voice raw.")
    p("A faint creak from the stair and then: 'Baba?' She stands at the top, dress torn, blue ribbon hanging by a thread.")
    p("For a long moment you only look at each other, then she runs and you catch her, and the world narrows to the breath between you.")
    state['found_mitali'] = True
    if state['has_dog']:
        p("Buro barks once — sharp and joyous — and curls near the door.")
    save_state(state)
    show_status(state, after_act=4)
    pm("Act IV complete. Run Act V when ready for the final aftermath.")

if __name__ == "__main__":
    act4_main()
