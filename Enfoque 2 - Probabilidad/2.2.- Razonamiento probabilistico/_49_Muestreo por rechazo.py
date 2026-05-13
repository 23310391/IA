'''
Muestreo por rechazo
'''

import random

# ====================== RED SIMPLE ==================================

def generar_muestra():

    lluvia = random.random() < 0.3

    # Si llueve, probablemente haya nubes
    if lluvia:
        nubes = random.random() < 0.8
    else:
        nubes = random.random() < 0.2

    return lluvia, nubes

# ====================== MUESTREO ====================================

def muestreo_rechazo(n=1000):

    aceptadas = 0
    lluvia_con_nubes = 0

    for _ in range(n):

        lluvia, nubes = generar_muestra()

        # Evidencia:
        # solo aceptar si hay nubes
        if nubes:

            aceptadas += 1

            if lluvia:
                lluvia_con_nubes += 1

    return lluvia_con_nubes / aceptadas

# ====================== EJECUCIÓN ===================================

resultado = muestreo_rechazo()

print("\nMuestreo por rechazo:\n")

print("P(Lluvia | Nubes) ≈")
print(round(resultado, 3))