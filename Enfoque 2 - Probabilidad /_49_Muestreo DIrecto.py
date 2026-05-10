'''
Muestreo directo
'''

import random

# ====================== DISTRIBUCIÓN ================================

P_clima = {
    'soleado': 0.7,
    'lluvia': 0.3
}

# ====================== MUESTREO ====================================

def muestreo_directo(n=1000):

    resultados = {
        'soleado': 0,
        'lluvia': 0
    }

    estados = list(P_clima.keys())
    probs = list(P_clima.values())

    for _ in range(n):
        muestra = random.choices(estados, weights=probs)[0]
        resultados[muestra] += 1

    return resultados

# ====================== EJECUCIÓN ===================================

resultado = muestreo_directo()

print("\nMuestreo Directo:\n")

for estado in resultado:
    print(
        estado,
        "→",
        resultado[estado] / 1000
    )