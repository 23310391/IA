'''
Probabilidad a priori
'''

import random

# ====================== PROBABILIDADES A PRIORI =======================

P = {
    'soleado': 0.7,
    'lluvia': 0.3
}

# ====================== SIMULACIÓN ====================================

def generar_clima():
    estados = list(P.keys())
    probs = list(P.values())

    return random.choices(estados, weights=probs)[0]

# ====================== EXPERIMENTO ===================================

resultados = {
    'soleado': 0,
    'lluvia': 0
}

simulaciones = 1000

for _ in range(simulaciones):
    clima = generar_clima()
    resultados[clima] += 1

# ====================== RESULTADOS ====================================

print("\nProbabilidades a priori:\n")

for estado in P:
    frecuencia = resultados[estado] / simulaciones

    print(f"{estado}:")
    print(f" A priori = {P[estado]}")
    print(f" Frecuencia observada = {frecuencia:.3f}")
    print()