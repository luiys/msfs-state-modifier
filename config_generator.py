import os
import json
from pathlib import Path

DEFAULT_PATH = os.path.join(
    str(Path.home()),
    "AppData",
    "Local",
    "Packages",
    "Microsoft.FlightSimulator_8wekyb3d8bbwe",
    "LocalState",
    "packages",
    "pmdg-aircraft-738",
    "work",
    "PanelState",
    "random_cold_and_dark_state.sav"
)

def generate_config():
    print("🔧 Gerador de configuração iniciado.")

    print(f"💡 Caminho padrão detectado:\n{DEFAULT_PATH}")
    custom_path = input("Deseja alterar o caminho? (S/N): ").strip().lower()

    final_path = DEFAULT_PATH
    if custom_path == "s":
        user_input = input("Digite o caminho completo do arquivo .sav: ").strip()
        if os.path.exists(os.path.dirname(user_input)):
            final_path = user_input
        else:
            print("❌ Caminho inválido. Usando o padrão.")

    config = {
        "panelStatePath": final_path
    }

    with open("config.json", "w") as file:
        json.dump(config, file, indent=4)
    
    print(f"✅ Caminho salvo com sucesso em config.json:\n{final_path}")

if __name__ == "__main__":
    generate_config()
