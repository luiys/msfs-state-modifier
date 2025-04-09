import os
import json
import random

# Caminho base fora do Program Files
BASE_DIR = os.path.join(os.environ["LOCALAPPDATA"], "MSFSStateModifier")
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")

def get_number_of_modifications() -> int:
    """
    Lê o perfil ativo do config.json (definido por 'selected_profile'),
    aplica a lógica de sorteios encadeados com base na configuração de
    'modification_probability_chain' e retorna o número de modificações.
    """

    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as file:
            config = json.load(file)
    except Exception as e:
        print(f"❌ Erro ao ler config.json: {e}")
        return 0

    # Extrai o nome do perfil selecionado
    profile_name = config.get("selected_profile", "natural").lower()
    print(f"[PERFIL CARREGADO] {profile_name}")

    # Busca o dicionário de perfis
    all_profiles = config.get("probability_profiles", {})

    # Busca o perfil selecionado dentro da estrutura
    profile = all_profiles.get(profile_name)

    if not profile or "modification_probability_chain" not in profile:
        print(f"⚠️ Perfil '{profile_name}' inválido ou sem configuração de probabilidade.")
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
