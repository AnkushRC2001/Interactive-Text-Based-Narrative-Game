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
    typewrite("# ASHES OF CALCUTTA", 0.02, style="bold underline")
    pl("## Act I — The Lockdown", style="bold")
    pm("(Rajendra Deb Lane, Calcutta — August 1946)", style="dim italic")
    pl("")

    # Scene 1 – The Sirens Begin (full descriptive text)
    p("Scene 1 – The Sirens Begin", style="bold")
    p("Monsoon clouds hung low over College Street, turning the afternoon the colour of old ink. The gutters frothed with paper pulp from the flooded bookstalls; the air smelled of wet jute, kerosene, and overripe bananas from the cart outside. Inside Sarkar & Sons General Store, a ceiling fan turned with a nervous buzz above rows of Dalda tins and biscuit jars.")
    p("Arunesh Chatterjee, thirty-eight, clerk and widower, counted the day’s takings while thinking of home — the narrow house on Rajendra Deb Lane, off Beadon Street, where his ten-year-old daughter Mitali waited with her blue ribbon and arithmetic notebook. He had promised to bring her lebu-biscuit and a new ink pen.")
    pl("The radio on the wall crackled.", style="warning")
    typewrite(" \"Akashvani Calcutta — Curfew from eight p.m. till dawn. Citizens are advised to remain indoors. Disturbances near Sealdah, Rajabazar, and Maniktala—\"", TYPE_DELAY, style="italic cyan")
    p("Static swallowed the voice, then the window rattled with a shout from outside. The smell of smoke seeped in. Somewhere down College Street a tram bell rang, then broke off mid-clang.", style="dim")
    p("'Lock the gate!' shouted the guard. The heavy shutter clanged down.", style="bold red")
    p("Arunesh gripped the counter. 'Open it! My meye is alone—Rajendra Deb Lane!'")
    p("The guard hesitated; the noise outside swelled — screams in two languages, boots running, glass breaking. When Arunesh lunged for the latch, the guard’s lathi came down in blind panic. White light flared behind his eyes, and the world fell away.")
    p("The last thing he saw was fire reflected in a puddle of rainwater.", style="bold red")
    pl("")

    # Scene 2 – The Back Room
    p("Scene 2 – The Back Room", style="bold")
    p("He woke to the slow drip of a leaking pipe. The single bulb flickered, casting a feverish yellow on sacks of rice split open across the floor. His head throbbed where the stick had landed; his fingers came away sticky with half-dried blood.")
    p("Outside, someone shouted a slogan, then the crack of gunfire, then silence.", style="dim")
    p("He whispered, 'Mitali… baba aschhe.'")
    p("A rustle came from behind the crates — a moan, low and human.", style="warning")
    pl("Choices:")
    c = present_choices([
        "Investigate the sound.",
        "Search the storeroom.",
        "Try the radio."
    ])

    # Investigate
    if c == 1:
        p("\nBehind the rice sacks crouched a boy, no older than twenty, his arm blistered. When the light touched him, he raised a pocketknife.")
        p("'Dada, thambo na! I’m not with them!'", style="italic")
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
            p("You tear a strip from your shirt and bind his wound. He exhales sharply and presses a small brass key into your hand. 'Back door. Go before they return.'")
            notify("Morality Increased (+2)", style="success")
            notify("He will remember that.", style="info")
        else:
            state['morality'] -= 2
            add_item(state, "rusty_knife")
            p("You slip the blade from his hand. He mutters, 'Even you fear me.'")
            notify("Morality Decreased (-2)", style="danger")
            notify("He will remember that.", style="info")

    # Search
    elif c == 2:
        p("\nShelves are overturned, tins dented. You find a half-tin of biscuits, a bottle of cloudy water, and a photograph — three smiling faces behind a counter. The father in a spotless dhoti. You set it back gently.")
        add_item(state, "biscuits")
        p("A trail of blood leads toward the rear alley door.")

    # Radio
    else:
        p("\nThe radio coughs static, then clears for a moment.")
        typewrite(" \"Violence spreads toward Beadon Street and Rajendra Deb Lane. Citizens advised—\"", TYPE_DELAY, style="italic cyan")
        p("The voice breaks apart. Arunesh’s knees weaken. 'Mitali… shona…'")
        p("The bulb flickers twice, then dies.")

    # Scene 3 — The Shutter
    pl("\nScene 3 — The Shutter", style="bold")
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
        p("The key turns with a clean click. You slip out into the rain and shadow.", style="success")
    elif "Force" in sel:
        p("You grip the hot metal...")
        # QTE
        if quick_time_event("MASH KEY TO FORCE OPEN", 2.0, lambda: None, lambda: None):
            p("With a heave, you force the shutter open just enough to slide through.", style="success")
            p("The hinge screams, but you are out.")
        else:
            state['health'] -= 2
            p("You fumble! The shutter slams back on your fingers.", style="danger")
            p("The noise attracts attention. Torchlight flares down the lane.", style="warning")
            notify("Health -2", style="danger")
    else:
        state['health'] -= 1
        p("You squeeze through a broken vent scraping rust across your arm.")
        notify("Health -1", style="danger")

    # Scene 4 — College Street Burning
    pl("\nScene 4 — College Street Burning", style="bold")
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
        p("You shove the cart aside, skin blistering. She gasps, 'Don’t take Amherst Street—too many dead there. Go by Beadon Road.'")
        notify("Morality +1", style="success")
        notify("Safe Route Unlocked", style="info")
    else:
        state['morality'] -= 1
        p("You turn away; the crackle of flame drowns her voice.")
        notify("Morality -1", style="danger")

    # Scene 5 — Rajendra Deb Lane
    pl("\nScene 5 — Rajendra Deb Lane", style="bold")
    p("The closer you get to home, the quieter the city grows. Houses stand like burnt shells; the sweet-shop at the corner, Bharat Misty Bhandar, lies gutted, syrup jars cracked open. Rain mixes with ash, carrying away bits of glass, bangles, the smell of ghee and smoke.")
    p("You turn into your lane. The streetlights are dead; only hurricane lamps flicker in the ruins. Each step sinks into mud and soot.")
    p("'Mitali… baba aschhe,' you whisper. No answer. Only the slow toll of the temple bell from Hedua Park.", style="dim")
    add_item(state, "found_ribbon")
    p("At your fence, something blue catches the light — a ribbon, frayed, blackened at the tips. You pick it up with trembling fingers.")
    p("'Thakur Gopal… raksha koro,' you murmur. 'Let her be safe.'")
    p("You square your shoulders and step toward the smouldering doorway of your home.")

    # Save and show status
    save_state(state)
    show_status(state, after_act=1)

    pm("Act I complete. The full game saves your current state to 'savegame.json'.", style="success")
    pm("When ready to continue (Act II), run the next act using the same engine/structure.")
    return state

if __name__ == "__main__":
    act1_main()
