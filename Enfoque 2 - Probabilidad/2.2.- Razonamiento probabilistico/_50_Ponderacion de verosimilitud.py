'''
Ponderación de verosimilitud
'''

import random

# ====================== PROBABILIDADES ================================

P_lluvia = 0.3

# P(Nubes | Lluvia)
P_nubes_dado_lluvia = {
    True: 0.8,
    False: 0.2
}

# ====================== MUESTREO ======================================

def ponderacion_verosimilitud(n=1000):

    peso_lluvia = 0
    peso_total = 0

    for _ in range(n):

        # Generar lluvia
        lluvia = random.random() < P_lluvia

        # Evidencia fija:
        # Nubes = True

        # Peso según evidencia
        peso = P_nubes_dado_lluvia[lluvia]

        # Acumular pesos
        peso_total += peso

        if lluvia:
            peso_lluvia += peso

    return peso_lluvia / peso_total

# ====================== EJECUCIÓN =====================================

resultado = ponderacion_verosimilitud()

print("\nPonderación de Verosimilitud:\n")

print("P(Lluvia | Nubes=True) ≈")
print(round(resultado, 3))