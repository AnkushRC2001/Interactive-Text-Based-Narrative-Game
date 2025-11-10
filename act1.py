# act1.py
# Act I for Ashes of Calcutta. Uses engine.py for printing/choices/state.
# Run: python act1.py

from engine import *
import random

def act1_main():
    # load or create state
    state = load_state()
    state['act'] = 1

    clear()
    typewrite("# ASHES OF CALCUTTA", 0.02)
    pl("## Act I — The Lockdown")
    pm("(Rajendra Deb Lane, Calcutta — August 1946)")
    pl("")

    # Scene 1 – The Sirens Begin (full descriptive text)
    p("Scene 1 – The Sirens Begin")
    p("Monsoon clouds hung low over College Street, turning the afternoon the colour of old ink. The gutters frothed with paper pulp from the flooded bookstalls; the air smelled of wet jute, kerosene, and overripe bananas from the cart outside. Inside Sarkar & Sons General Store, a ceiling fan turned with a nervous buzz above rows of Dalda tins and biscuit jars.")
    p("Arunesh Chatterjee, thirty-eight, clerk and widower, counted the day’s takings while thinking of home — the narrow house on Rajendra Deb Lane, off Beadon Street, where his ten-year-old daughter Mitali waited with her blue ribbon and arithmetic notebook. He had promised to bring her lebu-biscuit and a new ink pen.")
    pl("The radio on the wall crackled.")
    typewrite(" \"Akashvani Calcutta — Curfew from eight p.m. till dawn. Citizens are advised to remain indoors. Disturbances near Sealdah, Rajabazar, and Maniktala—\"", TYPE_DELAY)
    p("Static swallowed the voice, then the window rattled with a shout from outside. The smell of smoke seeped in. Somewhere down College Street a tram bell rang, then broke off mid-clang.")
    p("'Lock the gate!' shouted the guard. The heavy shutter clanged down.")
    p("Arunesh gripped the counter. 'Open it! My meye is alone—Rajendra Deb Lane!'")
    p("The guard hesitated; the noise outside swelled — screams in two languages, boots running, glass breaking. When Arunesh lunged for the latch, the guard’s lathi came down in blind panic. White light flared behind his eyes, and the world fell away.")
    p("The last thing he saw was fire reflected in a puddle of rainwater.")
    pl("")

    # Scene 2 – The Back Room
    p("Scene 2 – The Back Room")
    p("He woke to the slow drip of a leaking pipe. The single bulb flickered, casting a feverish yellow on sacks of rice split open across the floor. His head throbbed where the stick had landed; his fingers came away sticky with half-dried blood.")
    p("Outside, someone shouted a slogan, then the crack of gunfire, then silence.")
    p("He whispered, 'Mitali… baba aschhe.'")
    p("A rustle came from behind the crates — a moan, low and human.")
    pl("Choices:")
    c = present_choices([
        "Investigate the sound.",
        "Search the storeroom.",
        "Try the radio."
    ])

    # Investigate
    if c == 1:
        p("\nBehind the rice sacks crouched a boy, no older than twenty, his arm blistered. When the light touched him, he raised a pocketknife.")
        p("'Dada, thambo na! I’m not with them!'")
        p("His accent carried the roughness of Kidderpore docks. He was shaking.")
        p("Arunesh knelt. 'You’re hurt.'")
        p("The boy nodded. 'Fire… I ran when they came. Couldn’t tell who was who anymore.'")
        c2 = present_choices([
            "Help him — bind his wound.",
            "Take his knife."
        ])
        if c2 == 1:
            state['morality'] += 2
            add_item(state, "brass_key")
            p("You tear a strip from your shirt and bind his wound. He exhales sharply and presses a small brass key into your hand. 'Back door. Go before they return.' (morality +2)")
        else:
            state['morality'] -= 2
            add_item(state, "rusty_knife")
            p("You slip the blade from his hand. He mutters, 'Even you fear me.' (morality -2, gain Rusty Knife)")

    # Search
    elif c == 2:
        p("\nShelves are overturned, tins dented. You find a half-tin of biscuits, a bottle of cloudy water, and a photograph — three smiling faces behind a counter. The father in a spotless dhoti. You set it back gently.")
        add_item(state, "biscuits")
        p("A trail of blood leads toward the rear alley door.")

    # Radio
    else:
        p("\nThe radio coughs static, then clears for a moment.")
        typewrite(" \"Violence spreads toward Beadon Street and Rajendra Deb Lane. Citizens advised—\"", TYPE_DELAY)
        p("The voice breaks apart. Arunesh’s knees weaken. 'Mitali… shona…'")
        p("The bulb flickers twice, then dies.")

    # Scene 3 — The Shutter
    pl("\nScene 3 — The Shutter")
    p("The metal shutter burns hot to the touch. Outside, boots splash through water; someone cries out, then runs.")
    shutter_opts = []
    if has_item(state, "brass_key"):
        shutter_opts.append("Use the brass key — quiet escape.")
    shutter_opts.append("Force the shutter — lose health, make noise.")
    shutter_opts.append("Search for another exit — squeeze through a vent (scrape shoulder).")
    s = present_choices(shutter_opts)
    sel = shutter_opts[s-1]
    if sel.startswith("Use"):
        use_item(state, "brass_key")
        p("The key turns with a clean click. You slip out into the rain and shadow.")
    elif "Force" in sel:
        state['health'] -= 2
        p("You force the shutter. The hinge screams and torchlight flares down the lane. Your shoulder hurts.")
    else:
        state['health'] -= 1
        p("You squeeze through a broken vent scraping rust across your arm.")

    # Scene 4 — College Street Burning
    pl("\nScene 4 — College Street Burning")
    p("Rain begins again, thin and relentless. Pages from the bookstalls float in the drain — torn Gitanjali, school registers, detective magazines. A tram lies on its side near the Presidency College gate, wheels humming softly. The sky glows orange behind the University Senate House dome; smoke curls above Hedua Park.")
    p("From the crossroads comes a woman’s cry. 'Dada! Help koro!' She’s pinned beneath a fruit cart, fire licking its edges. Beyond her lies Beadon Street, your way home.")
    c4 = present_choices([
        "Help her — shove the cart aside.",
        "Leave her — turn away."
    ])
    if c4 == 1:
        state['morality'] += 1
        state['safe_route_unlocked'] = True
        add_item(state, "safe_route_note")
        p("You shove the cart aside, skin blistering. She gasps, 'Don’t take Amherst Street—too many dead there. Go by Beadon Road.' (morality +1, unlock Safe Route)")
    else:
        state['morality'] -= 1
        p("You turn away; the crackle of flame drowns her voice. (morality -1)")

    # Scene 5 — Rajendra Deb Lane
    pl("\nScene 5 — Rajendra Deb Lane")
    p("The closer you get to home, the quieter the city grows. Houses stand like burnt shells; the sweet-shop at the corner, Bharat Misty Bhandar, lies gutted, syrup jars cracked open. Rain mixes with ash, carrying away bits of glass, bangles, the smell of ghee and smoke.")
    p("You turn into your lane. The streetlights are dead; only hurricane lamps flicker in the ruins. Each step sinks into mud and soot.")
    p("'Mitali… baba aschhe,' you whisper. No answer. Only the slow toll of the temple bell from Hedua Park.")
    add_item(state, "found_ribbon")
    p("At your fence, something blue catches the light — a ribbon, frayed, blackened at the tips. You pick it up with trembling fingers.")
    p("'Thakur Gopal… raksha koro,' you murmur. 'Let her be safe.'")
    p("You square your shoulders and step toward the smouldering doorway of your home.")

    # Save and show status
    save_state(state)
    show_status(state, after_act=1)

    pm("Act I complete. The full game saves your current state to 'savegame.json'.")
    pm("When ready to continue (Act II), run the next act using the same engine/structure.")
    return state

if __name__ == "__main__":
    act1_main()
