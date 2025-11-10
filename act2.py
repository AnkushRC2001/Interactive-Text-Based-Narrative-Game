# act2.py
# Act II — The Crossing (full narrative & choices)
# Requires engine.py in same folder.

from engine import *
import random

def act2_main():
    state = load_state()
    state['act'] = 2
    clear()
    typewrite("# ASHES OF CALCUTTA", 0.02)
    pm("ACT II — THE CROSSING")
    pm("(Beadon Street / Bagbazar Ghat — August 1946)")
    pl("")

    # Scene 1 — Beadon Street Crossroads
    p("Scene 1 — Beadon Street Crossroads")
    p("Rain soaks the cracked tramlines. The smell of burnt cloth and incense hangs thick. The sound of chanting drifts from the south — slogans, gunfire, screams.")
    p("A police jeep lies overturned. A constable slumps beside it, his khaki shirt dark with blood. He raises a trembling hand.")
    p("'Help… the radio… please…'")
    choice = present_choices(["Help the constable", "Ignore him and move on"])
    if choice == 1:
        state['morality'] += 1
        add_item(state, "whistle")
        p("You kneel, lift him. The radio hisses that lines are cut. He breathes 'Evacuation… through Bagbazar Ghat.' He dies. You take his whistle. (morality +1)")
    else:
        state['morality'] -= 1
        p("You walk away. The man's plea dissolves in the rain. (morality -1)")

    # Scene 2 — Hedua Park Camp
    pl("\nScene 2 — Hedua Park Camp")
    p("The park has turned into a refugee camp — tents, ration barrels, frightened whispers. The statue of Prafulla Chandra Ray looms over the crowd, its marble streaked with rain.")
    p("A young nurse calls out: 'If you’re looking for family, write the name! We’ll try the registers!'")
    p("You scrawl 'Mitali Chatterjee' on a damp sheet.")
    c2 = present_choices(["Thank her and leave immediately", "Stay to help treat the wounded"])
    if c2 == 2:
        state['morality'] += 1
        add_item(state, "silver_locket")
        p("You tend the wounded; a nurse presses a silver locket into your palm. 'Maybe it will bring you luck.' (morality +1)")
    else:
        p("You leave the camp to head for the river. The thought of Mitali sharpens your steps.")

    # Scene 3 — Bagbazar Ghat
    pl("\nScene 3 — Bagbazar Ghat")
    p("The riverfront is chaos. Boats sway as hundreds press forward. The boatman sits on his haunches and asks for payment.")
    options = []
    if has_item(state, "silver_locket"):
        options.append("Offer the silver locket")
    if has_item(state, "rusty_knife"):
        options.append("Threaten him with your rusty knife")
    options.append("Beg for passage — plead for your daughter")
    ch = present_choices(options)
    chosen = options[ch-1]
    if "locket" in chosen:
        state['morality'] += 1
        state['route'] = "river"
        use_item(state, "silver_locket")
        p("The boatman takes the locket gently. 'Keep your seat, babu. We’ll cross before dawn.' (morality +1)")
    elif "Threaten" in chosen:
        state['morality'] -= 2
        state['route'] = "river"
        p("You flash the knife and force him to row. The oar cuts the oily water. (morality -2)")
    else:
        # 50/50 chance
        if random.choice([True, False]):
            state['route'] = "river"
            p("The boatman hesitates, then nods. 'For a father.' You cross.")
        else:
            state['route'] = "ground"
            p("He refuses. 'Too much blood tonight.' You must take the ground route through Sovabazar.")

    # Scene 4A — River Crossing
    if state['route'] == "river":
        pl("\nScene 4A — The River Crossing")
        p("The oar dips in rhythm. Warehouses along Strand Road glow like embers. A woman sobs beside you, holding a bundle that doesn’t move.")
        c = present_choices(["Shield the woman with your body (morality +1, lose health)", "Stay low and let fate decide"])
        if c == 1:
            state['morality'] += 1
            state['health'] -= 1
            p("You shield her. A bullet grazes your arm. She whispers, 'Bless you, dada.' (health -1, morality +1)")
        else:
            p("You stay low. The boat drifts under the burning sky, each ripple reflecting a flare of orange.")
        # Reunion chance
        if state['morality'] >= 2:
            state['found_mitali'] = True
            p("Across the bank, a child's voice calls: 'Baba!' Mitali runs to you as you stagger ashore.")
        else:
            p("You arrive alone. Refugees scatter. A child’s sandal lies in the mud — a painful sign you are not there yet.")

    # Scene 5B — Ground Route
    else:
        pl("\nScene 5B — The Ground Route (Sovabazar & Nimtala)")
        p("You weave through Sovabazar lanes. The smell of burnt paint and wet dust fills your lungs.")
        c = present_choices(["Help the old man trapped under a balcony beam", "Ignore and move on"])
        if c == 1:
            state['morality'] += 1
            add_item(state, "directions_to_nimtala")
            state['directions_to_nimtala'] = True
            p("The old man whispers, 'Go by Nimtala… when you smell salt you're near.' He dies. (morality +1)")
        else:
            state['morality'] -= 1
            state['health'] -= 1
            p("You move on. The old man's breath stops, and you carry the guilt. (health -1, morality -1)")
        p("You reach Nimtala Ghat; bodies float on the steps.")
        c2 = present_choices(["Take the ferry yourself (dangerous)", "Wait and join a group of refugees (safer)"])
        if c2 == 1:
            state['morality'] -= 1
            state['health'] -= 1
            p("You row alone, coughing and bleeding. The far bank takes you at dawn. (health -1, morality -1)")
        else:
            state['morality'] += 1
            p("You join others. They chant for protection as hands pull each other in. The group slows risk through solidarity. (morality +1)")
        if state['morality'] >= 2 and state.get('directions_to_nimtala', False):
            state['found_mitali'] = True
            p("A girl's voice rings out: 'Baba!' You find Mitali among the crowd and embrace her.")
        else:
            p("You come ashore alone. Only a blue ribbon drifts by your feet.")

    save_state(state)
    show_status(state, after_act=2)
    pm("Act II complete. Run Act III when ready.")

if __name__ == "__main__":
    act2_main()
