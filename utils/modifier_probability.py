import os
import json
import random

# Base path outside Program Files
BASE_DIR = os.path.join(os.environ["LOCALAPPDATA"], "MSFSStateModifier")
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")

def get_number_of_modifications() -> int:
    """
    Reads the active profile from config.json (defined by 'selected_profile'),
    applies the chained random chance logic based on the 
    'modification_probability_chain', and returns the number of modifications.
    """

    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as file:
            config = json.load(file)
    except Exception as e:
        print(f"❌ Error reading config.json: {e}")
        return 0

    # Extract the selected profile name
    profile_name = config.get("selected_profile", "realistic").lower()
    print(f"[LOADED PROFILE] {profile_name}")

    # Get all available profiles
    all_profiles = config.get("probability_profiles", {})

    # Get the selected profile from the structure
    profile = all_profiles.get(profile_name)

    if not profile or "modification_probability_chain" not in profile:
        print(f"⚠️ Profile '{profile_name}' is invalid or missing probability chain.")
        return 0

    chain = profile["modification_probability_chain"]

    modifications = 0

    for key in sorted(chain.keys(), key=lambda x: int(x)):
        chance = chain[key]
        roll = random.random()
        if roll < chance:
            modifications = int(key)
        else:
            break

    return modifications
