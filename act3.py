# act3.py
# Act III — The Road to Tikiapara (full narrative & choices)
# Requires engine.py and savegame.json from previous acts.

from engine import *
import random

def act3_main():
    state = load_state()
    state['act'] = 3
    clear()
    typewrite("# ASHES OF CALCUTTA", 0.02)
    pm("ACT III — THE ROAD TO TIKIAPARA")
    pm("(Howrah Side, Pre-dawn — August 1946)")
    pl("")

    p("Scene 1 — Dawn Among the Ruins")
    p("The first gray light struggles through a curtain of rain. Mud clings to Arunesh's feet as he trudges along the riverbank. The Hooghly flows sluggishly, swollen with monsoon water, carrying charred debris and paper.")
    p("The blue ribbon in his hand is cold and wet, a fragile proof that Mitali exists.")
    pl("A low, trembling whimper breaks through the silence.")

    # Scene 1 — The Dog
    p("Under an overturned handcart, a small mongrel lies trapped — one leg bent unnaturally, eyes wide with terror. Flies circle; the animal whines.")
    c = present_choices(["Help the dog — bind and free it", "Leave it and keep moving"])
    if c == 1:
        state['has_dog'] = True
        add_item(state, "buro")
        state['morality'] += 2
        p("You tear a strip and bind the leg. Lifting the cart, the dog limps free and presses its muzzle to your knee. It follows you. (Companion: Buro; morality +2)")
    else:
        state['morality'] -= 1
        p("You walk on. The whimper fades behind you and you feel the small weight of the choice.")

    # Scene 2 — Pilkhana Road
    pl("\nScene 2 — Pilkhana Road")
    p("Pilkhana Road twists past ruined stables and roofless huts. A barricade of planks blocks the path; men with soot-darkened faces stand guard.")
    c2 = present_choices(["Speak calmly and plead passage", "Fight your way through", "Sneak around"])
    if c2 == 1:
        state['morality'] += 1
        p("You speak of fathers and daughters. The leader's eyes soften and he gestures you through. (morality +1)")
    elif c2 == 2:
        state['morality'] -= 2
        state['health'] -= 2
        p("A fight erupts; you push through but blood wets your sleeve. (health -2, morality -2)")
    else:
        if state['has_dog']:
            p("Buro's low growl warns you of a patrol. You slip past unseen.")
        else:
            state['health'] -= 1
            p("A thrown brick grazes your shoulder as you sneak through. (health -1)")

    # Scene 3 — Trainyard clue
    pl("\nScene 3 — The Trainyard")
    p("The goods yard is a tomb of iron. A boy bursts from a half-flooded carriage clutching biscuits.")
    p("'Don't tell them, dada!' he gasps. 'I saw a girl — blue ribbon. She went back to Calcutta. She was crying.'")
    p("The name Mitali hits you like a physical blow.")

    # Scene 4 — Tikiapara Camp
    pl("\nScene 4 — Tikiapara Camp")
    p("By late afternoon the camp sags under rain. Tarpaulins flap; children shiver.")
    p("A caretaker flips through the ledger: 'Chatterjee… Rajendra Deb Lane? There was a girl. She said she would go back — that her father would come.'")
    p("Your chest tightens. 'She went back… to Calcutta?' you whisper. Hope and dread tangle inside you.")
    if state['has_dog']:
        p("Buro presses close, a living anchor at your side.")
    save_state(state)
    show_status(state, after_act=3)
    pm("Act III complete. Run Act IV to continue the return to Calcutta.")

if __name__ == "__main__":
    act3_main()
