import os
import random
import json
import shutil
import sys
import logging
from utils.modifier_probability import get_number_of_modifications

# Caminho base fora do Program Files
BASE_DIR = os.path.join(os.environ["LOCALAPPDATA"], "MSFSStateModifier")
os.makedirs(BASE_DIR, exist_ok=True)

# Configurar log de modificação
log_file = os.path.join(BASE_DIR, "modification.log")
modifier_logger = logging.getLogger("state_modifier_logger")
modifier_logger.setLevel(logging.INFO)

if not modifier_logger.handlers:
    handler = logging.FileHandler(log_file, encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)
    modifier_logger.addHandler(handler)

# Carrega configurações
with open(os.path.join(BASE_DIR, "config.json"), "r") as file:
    config = json.load(file)

# Caminhos dos arquivos de estado
ORIGINAL_STATE_PATH = os.path.join(BASE_DIR, config["original_state_path"])
MODIFIED_STATE_PATH = os.path.join(BASE_DIR, config["modified_state_path"])
FINAL_STATE_PATH = config["final_state_path"]

# Novas configs de modificação
BUTTONS = config.get("recommended_buttons", [])
PROBABILITY_CHAIN = config.get("modification_probability_chain", {})
MAX_BUTTONS_TO_MODIFY = config.get("max_buttons_to_modify", 8)

def read_state_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

def write_state_file(file_path, lines):
    with open(file_path, "w") as file:
        file.writelines(lines)

def get_random_value(button, current_value):
    clean_value = str(current_value).strip()
    btn_type = button.get("type")

    if btn_type == "binary":
        return "1" if clean_value == "0" else "0"

    if btn_type == "int":
        min_val = int(button.get("min", 0))
        max_val = int(button.get("max", 1))
        current_int = int(clean_value)
        options = [val for val in range(min_val, max_val + 1) if val != current_int]
        return str(random.choice(options)) if options else str(current_int)

    if btn_type == "range":
        min_val = float(button.get("min", 0))
        max_val = float(button.get("max", 1))
        current_float = float(clean_value)
        new_val = current_float
        while new_val == current_float:
            new_val = round(random.uniform(min_val, max_val), 2)
        return str(new_val)

    if btn_type == "enum":
        values = button.get("values", [])
        if not values:
            return current_value
        options = [val for val in values if val != clean_value]
        return random.choice(options) if options else clean_value

    return current_value

def modify_state(lines):
    lines_copy = lines[:]
    modified_count = 0
    changes_log = []

    # Aplica a lógica encadeada
    num_modifications = get_number_of_modifications(PROBABILITY_CHAIN)
    num_modifications = min(num_modifications, MAX_BUTTONS_TO_MODIFY, len(BUTTONS))

    if num_modifications == 0:
        modifier_logger.info("🎲 Sorteio não selecionou nenhuma modificação.")
        return lines

    buttons_to_modify = random.sample(BUTTONS, num_modifications)

    for button in buttons_to_modify:
        button_name = button["name"]
        for i, line in enumerate(lines_copy):
            if line.startswith(button_name + "="):
                key, value = line.strip().split("=")
                new_value = get_random_value(button, value)
                print(f"🔍 [{key}] valor atual: {repr(value)} | 🔁 Novo valor calculado {new_value}")
                lines_copy[i] = f"{key}={new_value}\n"
                changes_log.append(f"{key}: {value} → {new_value}")
                modified_count += 1
                break

    if changes_log:
        modifier_logger.info("---- Nova execução do modificador ----")
        for change in changes_log:
            modifier_logger.info(f"{change}")
        modifier_logger.info(f"Total de alterações: {modified_count}")

    return lines_copy

def main():
    original_lines = read_state_file(ORIGINAL_STATE_PATH)
    modified_lines = modify_state(original_lines)

    if modified_lines != original_lines:
        write_state_file(MODIFIED_STATE_PATH, modified_lines)
        shutil.copy(MODIFIED_STATE_PATH, FINAL_STATE_PATH)
        modifier_logger.info(f"Modificações aplicadas e copiadas para: {FINAL_STATE_PATH}")
    else:
        shutil.copy(ORIGINAL_STATE_PATH, FINAL_STATE_PATH)
        modifier_logger.info("Estado original mantido (nenhuma alteração feita).")

if __name__ == "__main__":
    main()
