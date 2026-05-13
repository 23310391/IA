'''
Incertidumbre probabilística
Simulación simple
'''

import random

# ====================== PROBABILIDADES ================================

# Probabilidades del clima
probabilidades = {
    'soleado': 0.6,
    'lluvia': 0.3,
    'tormenta': 0.1
}

# ====================== SIMULACIÓN ====================================

def generar_clima():
    estados = list(probabilidades.keys())
    probs = list(probabilidades.values())

    return random.choices(estados, weights=probs)[0]

# ====================== EXPERIMENTO ===================================

resultados = {
    'soleado': 0,
    'lluvia': 0,
    'tormenta': 0
}

simulaciones = 1000

for _ in range(simulaciones):
    clima = generar_clima()
    resultados[clima] += 1

# ====================== RESULTADOS ====================================

print("\nResultados:\n")

for estado in resultados:
    frecuencia = resultados[estado] / simulaciones

    print(f"{estado}:")
    print(f" Frecuencia observada = {frecuencia:.3f}")
    print(f" Probabilidad esperada = {probabilidades[estado]}")
    print()