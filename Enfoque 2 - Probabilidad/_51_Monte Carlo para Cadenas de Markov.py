'''
Monte Carlo para Cadenas de Markov (MCMC)
'''

import random

# ====================== TRANSICIONES ================================

transiciones = {

    'soleado': {
        'soleado': 0.8,
        'lluvia': 0.2
    },

    'lluvia': {
        'soleado': 0.4,
        'lluvia': 0.6
    }
}

# ====================== CADENA DE MARKOV =============================

def siguiente_estado(actual):

    probs = transiciones[actual]

    estados = list(probs.keys())
    probabilidades = list(probs.values())

    return random.choices(
        estados,
        weights=probabilidades
    )[0]

# ====================== MCMC =========================================

def mcmc(inicio='soleado', pasos=1000):

    actual = inicio

    conteo = {
        'soleado': 0,
        'lluvia': 0
    }

    historial = [actual]

    for _ in range(pasos):

        actual = siguiente_estado(actual)

        conteo[actual] += 1

        historial.append(actual)

    return conteo, historial

# ====================== EJECUCIÓN ====================================

conteo, historial = mcmc()

print("\nMCMC:\n")

print("Frecuencias:")

for estado in conteo:
    print(
        estado,
        "→",
        round(conteo[estado] / 1000, 3)
    )

print("\nPrimeros estados:")
print(historial[:20])