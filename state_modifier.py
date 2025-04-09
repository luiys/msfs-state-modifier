import os
import random
import json
import shutil
import sys

# Caminho base seguro fora do Program Files
BASE_DIR = os.path.join(os.environ["LOCALAPPDATA"], "MSFSStateModifier")

# Carrega configurações do config.json
print(f"🔧 BASE_DIR: {BASE_DIR}")
with open(os.path.join(BASE_DIR, "config.json"), "r") as file:
    config = json.load(file)

# Caminhos
ORIGINAL_STATE_PATH = os.path.join(BASE_DIR, config["original_state_path"])
MODIFIED_STATE_PATH = os.path.join(BASE_DIR, config["modified_state_path"])
FINAL_STATE_PATH = config["final_state_path"]

MODIFICATION_PROBABILITY = config.get("modification_probability", 0.2)
RECOMMENDED_BUTTONS = config.get("recommended_buttons", [])
MAX_BUTTONS_TO_MODIFY = config.get("max_buttons_to_modify", 3)

def read_state_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

def write_state_file(file_path, lines):
    with open(file_path, "w") as file:
        file.writelines(lines)

def modify_state(lines):
    lines_copy = lines[:]
    modified_count = 0
    buttons_to_modify = random.sample(RECOMMENDED_BUTTONS, min(MAX_BUTTONS_TO_MODIFY, len(RECOMMENDED_BUTTONS)))

    for button in buttons_to_modify:
        for i, line in enumerate(lines_copy):
            if line.startswith(button + "="):
                key, value = line.strip().split("=")
                new_value = "1" if value == "0" else "0"
                lines_copy[i] = f"{key}={new_value}\n"
                print(f"Modified: {key} to {new_value}")
                modified_count += 1
                break

    print(f"🔧 Total de botões modificados: {modified_count}")
    return lines_copy

def main():
    original_lines = read_state_file(ORIGINAL_STATE_PATH)

    if random.random() < MODIFICATION_PROBABILITY:
        print("Modifying the state file...")
        modified_lines = modify_state(original_lines)
        write_state_file(MODIFIED_STATE_PATH, modified_lines)
        shutil.copy(MODIFIED_STATE_PATH, FINAL_STATE_PATH)
        print(f"Modified state file has been applied. [{FINAL_STATE_PATH}]")
    else:
        shutil.copy(ORIGINAL_STATE_PATH, FINAL_STATE_PATH)
        print("No modification needed. Using the original state file.")

if __name__ == "__main__":
    main()
