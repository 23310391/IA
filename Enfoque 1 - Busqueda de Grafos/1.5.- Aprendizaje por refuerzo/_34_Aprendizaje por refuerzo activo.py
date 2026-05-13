'''
Aprendizaje por Refuerzo Activo
Q-Learning
'''

import random

# ====================== ESTADOS =======================================

estados = ['A', 'B', 'C']
objetivo = 'C'

# ====================== ACCIONES ======================================

acciones = ['avanzar', 'quedarse']

# ====================== TRANSICIONES ================================

transiciones = {
    'A': {
        'avanzar': [('B', 1.0)],
        'quedarse': [('A', 1.0)]
    },
    'B': {
        'avanzar': [('C', 1.0)],
        'quedarse': [('B', 1.0)]
    },
    'C': {
        'avanzar': [('C', 1.0)],
        'quedarse': [('C', 1.0)]
    }
}

# ====================== RECOMPENSAS ==================================

def recompensa(s):
    return 100 if s == objetivo else -1

# ====================== PARÁMETROS ====================================

alpha = 0.1   # tasa de aprendizaje
gamma = 0.9   # descuento
epsilon = 0.2 # exploración

# ====================== INICIALIZAR Q ================================

Q = {}
for s in estados:
    Q[s] = {a: 0 for a in acciones}

# ====================== FUNCIONES =====================================

def siguiente_estado(s, a):
    posibles = transiciones[s][a]
    estados_s = [x for x, _ in posibles]
    probs = [p for _, p in posibles]
    return random.choices(estados_s, weights=probs)[0]

def elegir_accion(s):
    # epsilon-greedy
    if random.random() < epsilon:
        return random.choice(acciones)
    return max(Q[s], key=Q[s].get)

# ====================== Q-LEARNING ====================================

def q_learning(episodios=30):
    global Q

    for ep in range(episodios):
        estado = 'A'

        print(f"\nEpisodio {ep+1}")

        while estado != objetivo:
            accion = elegir_accion(estado)
            siguiente = siguiente_estado(estado, accion)

            r = recompensa(siguiente)

            # 🔹 actualización Q
            mejor_siguiente = max(Q[siguiente].values())
            Q[estado][accion] += alpha * (
                r + gamma * mejor_siguiente - Q[estado][accion]
            )

            print(f"{estado} --{accion}--> {siguiente} | Q = {Q[estado][accion]:.2f}")

            estado = siguiente

    print("\nQ final:")
    for s in Q:
        print(s, Q[s])

    print("\nPolítica aprendida:")
    for s in estados:
        mejor = max(Q[s], key=Q[s].get)
        print(f"{s} → {mejor}")

# ====================== EJECUCIÓN =====================================

q_learning()