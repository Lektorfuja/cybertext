import random

def generate_cyberpunk_story():
    """Generates a short cyberpunk story with 100 characters and saves it to a text file."""

    # --- Character Name and Appearance Generators ---
    prefixes = ["Neo-", "Cyber-", "Tech-", "Data-", "Synth-", "Shadow-", "Chrome-", "Steel-", "Neon-", "Void-"]
    suffixes = ["Runner", "Blade", "Ghost", "Mage", "Shade", "Punk", "Dancer", "Whisper", "Glitch", "Surge"]
    augmentations = ["cybernetic eyes", "neural implants", "enhanced limbs", "data jacks", "optical camouflage", "bio-engineered skin", "internal comms", "reflex boosters", "memory chips", "vocal modulator"]
    clothing = ["worn leather jacket", "chrome-plated armor", "fiber-optic trench coat", "dataweave jumpsuit", "patched-up synth-leather", "glowing neon vest", "adaptive camouflage suit", "reinforced polymer weave", "holographic t-shirt", "thermal regulating gear"]
    hair_styles = ["shaved with neon streaks", "cybernetic implants woven in", "long and matted", "brightly dyed mohawk", "short and functional", "data cables braided in", "augmented reality display embedded", "slicked back and gelled", "wild and untamed", "color-shifting strands"]

    def generate_character_name():
        return random.choice(prefixes) + random.choice(suffixes)

    def generate_character_appearance():
        appearance = f"with {random.choice(augmentations)}, wearing a {random.choice(clothing)}, and sporting {random.choice(hair_styles)}."
        return appearance

    # --- Location and Setting Generators ---
    city_districts = ["the Neon Slums", "the Glitch Markets", "the Corporate Spire", "the Undercity Docks", "the Data Havens", "the Industrial Zone", "the Pleasure Domes", "the Skyways", "the Forgotten Sectors", "the Orbital Platforms"]
    atmospheres = ["rain-slicked streets", "holographic advertisements flickering", "the constant hum of machinery", "the smell of synth-noodles and ozone", "a thick smog hanging in the air", "glimmering neon signs reflecting", "the distant rumble of hovercars", "encrypted data streams flowing visibly", "the oppressive silence of the upper levels", "the chaotic energy of the lower depths"]

    def generate_location():
        return random.choice(city_districts)

    def generate_atmosphere():
        return random.choice(atmospheres)

    # --- Plot Element Generators ---
    motivations = ["retrieving stolen data", "escaping corporate security", "seeking a rare cybernetic upgrade", "delivering a crucial package", "uncovering a conspiracy", "seeking revenge", "making a vital connection", "surviving another night", "finding a lost loved one", "uploading a dangerous virus"]
    challenges = ["a sudden security lockdown", "a rival gang ambush", "a malfunctioning implant", "a relentless bounty hunter", "encrypted firewalls", "corrupt officials", "a double-cross", "environmental hazards", "a ticking time bomb", "psychological warfare"]
    twists = ["a surprising ally appears", "the target is not who they seem", "a hidden agenda is revealed", "a dangerous secret is uncovered", "the lines between reality and simulation blur", "an unexpected betrayal", "a moral dilemma arises", "a chance encounter changes everything", "a forgotten memory resurfaces", "the mission's true purpose is unveiled"]

    def generate_motivation():
        return random.choice(motivations)

    def generate_challenge():
        return random.choice(challenges)

    def generate_twist():
        return random.choice(twists)

    # --- Story Generation ---
    character_name = generate_character_name()
    character_appearance = generate_character_appearance()
    location = generate_location()
    atmosphere = generate_atmosphere()
    motivation = generate_motivation()
    challenge = generate_challenge()
    twist = generate_twist()

    story = f"The neon glow of {location} painted {atmosphere} as {character_name}, {character_appearance}, moved with a practiced stealth. Their current objective: {motivation}. But the gritty reality of the cyberpunk sprawl soon crashed in, manifesting as {challenge}. Just when the odds seemed insurmountable, {twist}."

    # --- Save to File ---
    filename = "cyberpunk_story.txt"
    with open(filename, "w") as f:
        f.write(story)

    print(f"Cyberpunk story generated and saved to '{filename}'")

if __name__ == "__main__":
    generate_cyberpunk_story()
