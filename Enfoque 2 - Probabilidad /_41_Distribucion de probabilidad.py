'''
Distribución de probabilidad
Ejemplo con un dado
'''

import random

# ====================== DISTRIBUCIÓN ==================================

distribucion = {
    1: 1/6,
    2: 1/6,
    3: 1/6,
    4: 1/6,
    5: 1/6,
    6: 1/6
}

# ====================== SIMULACIÓN ====================================

resultados = {i: 0 for i in range(1, 7)}

lanzamientos = 1000

for _ in range(lanzamientos):
    dado = random.randint(1, 6)
    resultados[dado] += 1

# ====================== RESULTADOS ====================================

print("\nDistribución de probabilidad:\n")

for valor in distribucion:
    frecuencia = resultados[valor] / lanzamientos

    print(f"Valor {valor}:")
    print(f" Probabilidad teórica = {distribucion[valor]:.3f}")
    print(f" Frecuencia observada = {frecuencia:.3f}")
    print()