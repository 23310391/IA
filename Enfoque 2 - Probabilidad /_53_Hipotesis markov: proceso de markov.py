'''
Hipótesis de Markov
Proceso de Markov simple
'''

import random

# ====================== TRANSICIONES ================================

# El siguiente estado depende SOLO del actual
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

# ====================== PROCESO DE MARKOV ============================

def proceso_markov(inicio='soleado', pasos=15):

    actual = inicio

    historial = [actual]

    for _ in range(pasos):

        # SOLO usa el estado actual
        actual = siguiente_estado(actual)

        historial.append(actual)

    return historial

# ====================== EJECUCIÓN ===================================

historial = proceso_markov()

print("\nProceso de Markov:\n")

for i, estado in enumerate(historial):
    print(f"Tiempo {i}: {estado}")