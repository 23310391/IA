'''
POMDP (MDP parcialmente observable)
Actualización de creencias + decisión
'''

import random

# ====================== ESTADOS =======================================

estados = ['A', 'B', 'C']
objetivo = 'C'

# ====================== ACCIONES ======================================

acciones = ['avanzar', 'quedarse']

# ====================== TRANSICIONES ================================

transiciones = {
    'A': {'avanzar': [('B', 0.8), ('A', 0.2)], 'quedarse': [('A', 1.0)]},
    'B': {'avanzar': [('C', 0.9), ('B', 0.1)], 'quedarse': [('B', 1.0)]},
    'C': {'avanzar': [('C', 1.0)], 'quedarse': [('C', 1.0)]}
}

# ====================== OBSERVACIONES ================================

observaciones = ['cerca', 'lejos']

# P(obs | estado)
modelo_obs = {
    'A': {'lejos': 0.8, 'cerca': 0.2},
    'B': {'lejos': 0.3, 'cerca': 0.7},
    'C': {'lejos': 0.1, 'cerca': 0.9}
}

# ====================== RECOMPENSAS ==================================

def recompensa(s):
    return 100 if s == objetivo else -1

# ====================== BELIEF INICIAL ===============================

belief = {
    'A': 0.6,
    'B': 0.3,
    'C': 0.1
}

# ====================== ACTUALIZACIÓN DE BELIEF =======================

def actualizar_belief(belief, accion, observacion):
    nuevo_belief = {}

    for s_next in estados:
        prob = 0

        for s in estados:
            # P(s -> s_next)
            for s2, p_trans in transiciones[s][accion]:
                if s2 == s_next:
                    prob += belief[s] * p_trans

        # multiplicar por probabilidad de observación
        prob *= modelo_obs[s_next][observacion]

        nuevo_belief[s_next] = prob

    # normalizar
    total = sum(nuevo_belief.values())
    for s in nuevo_belief:
        nuevo_belief[s] /= total

    return nuevo_belief

# ====================== SELECCIÓN DE ACCIÓN ==========================

def elegir_accion(belief):
    # estrategia simple: si crees que estás cerca → avanzar
    if belief['C'] > 0.5 or belief['B'] > 0.5:
        return 'avanzar'
    return 'quedarse'

# ====================== SIMULACIÓN ====================================

def simular(pasos=5):
    global belief

    estado_real = random.choice(estados)

    print("\nSimulación POMDP:\n")

    for t in range(pasos):
        accion = elegir_accion(belief)

        # transición real
        posibles = transiciones[estado_real][accion]
        estados_siguientes = [s for s, _ in posibles]
        probs = [p for _, p in posibles]
        estado_real = random.choices(estados_siguientes, weights=probs)[0]

        # generar observación
        obs_probs = modelo_obs[estado_real]
        obs = random.choices(list(obs_probs.keys()), weights=obs_probs.values())[0]

        # actualizar creencia
        belief = actualizar_belief(belief, accion, obs)

        print(f"Paso {t}:")
        print(f"Acción: {accion}")
        print(f"Observación: {obs}")
        print(f"Creencia: {belief}\n")

        if estado_real == objetivo:
            print("¡Objetivo alcanzado!")
            break

# ====================== EJECUCIÓN =====================================

simular()