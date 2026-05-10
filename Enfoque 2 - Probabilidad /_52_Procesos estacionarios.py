'''
Proceso estacionario
Cadena de Markov simple
'''

import random

# ====================== TRANSICIONES ================================

# Las probabilidades NO cambian con el tiempo
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

# ====================== SIGUIENTE ESTADO =============================

def siguiente_estado(actual):

    estados = list(transiciones[actual].keys())
    probs = list(transiciones[actual].values())

    return random.choices(
        estados,
        weights=probs
    )[0]

# ====================== SIMULACIÓN ==================================

def proceso_estacionario(inicio='soleado', pasos=20):

    actual = inicio

    historial = [actual]

    for _ in range(pasos):

        actual = siguiente_estado(actual)

        historial.append(actual)

    return historial

# ====================== EJECUCIÓN ===================================

historial = proceso_estacionario()

print("\nProceso estacionario:\n")

for i, estado in enumerate(historial):
    print(f"Tiempo {i}: {estado}")