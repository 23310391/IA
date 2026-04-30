'''
Proceso de Decisión de Markov (MDP)
Simulación de un agente siguiendo una política
'''

import random

# ====================== ESTADOS =======================================

estados = ['A', 'B', 'C']
objetivo = 'C'

# ====================== ACCIONES ======================================

acciones = ['avanzar', 'quedarse']

# ====================== TRANSICIONES ================================

# P(s' | s, a)
transiciones = {
    'A': {
        'avanzar': [('B', 0.8), ('A', 0.2)],  # a veces falla
        'quedarse': [('A', 1.0)]
    },
    'B': {
        'avanzar': [('C', 0.9), ('B', 0.1)],
        'quedarse': [('B', 1.0)]
    },
    'C': {
        'avanzar': [('C', 1.0)],
        'quedarse': [('C', 1.0)]
    }
}

# ====================== RECOMPENSAS ==================================

def recompensa(s, a, s_next):
    if s_next == objetivo:
        return 100
    return -1

# ====================== POLÍTICA ======================================

# Política (puede venir de value iteration o policy iteration)
politica = {
    'A': 'avanzar',
    'B': 'avanzar',
    'C': 'quedarse'
}

# ====================== SIMULACIÓN ====================================

def elegir_siguiente(estado, accion):
    posibles = transiciones[estado][accion]
    
    estados_siguientes = [s for s, _ in posibles]
    probabilidades = [p for _, p in posibles]

    return random.choices(estados_siguientes, weights=probabilidades)[0]

# ====================== EJECUCIÓN =====================================

def simular(inicio, pasos=10):
    estado = inicio
    total_recompensa = 0

    print("\nSimulación del MDP:\n")

    for t in range(pasos):
        accion = politica[estado]
        siguiente = elegir_siguiente(estado, accion)
        r = recompensa(estado, accion, siguiente)

        print(f"Paso {t}:")
        print(f"Estado: {estado}")
        print(f"Acción: {accion}")
        print(f"Siguiente: {siguiente}")
        print(f"Recompensa: {r}\n")

        total_recompensa += r
        estado = siguiente

        if estado == objetivo:
            print("¡Objetivo alcanzado!\n")
            break

    print("Recompensa total:", total_recompensa)

# ====================== INICIO ========================================

simular('A')