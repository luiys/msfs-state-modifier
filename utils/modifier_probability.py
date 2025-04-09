import random

def get_number_of_modifications(probability_chain: dict) -> int:
    """
    Recebe um dicionário com a estrutura:
    {
        "1": 0.5,
        "2": 0.4,
        "3": 0.3,
        ...
    }

    E retorna a quantidade de modificações com base em sorteios encadeados.
    """

    modifications = 0

    # Garante que as chaves serão processadas em ordem crescente
    for key in sorted(probability_chain.keys(), key=lambda x: int(x)):
        chance = probability_chain[key]
        roll = random.random()

        if roll < chance:
            modifications = int(key)
        else:
            break  # Falhou no sorteio, para aqui

    return modifications
