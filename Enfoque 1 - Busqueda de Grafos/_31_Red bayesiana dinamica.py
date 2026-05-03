'''
Red Bayesiana Dinámica (DBN)
Filtrado hacia adelante (Forward)
'''

# ====================== ESTADOS =======================================

ESTADOS = ['Sano', 'Enfermo']
OBSERVACIONES = ['Normal', 'Fiebre']

# ====================== PROBABILIDADES ================================

# Probabilidad inicial P(X0)
PI = {
    'Sano': 0.8,
    'Enfermo': 0.2
}

# Transición P(Xt | Xt-1)
TRANSICION = {
    'Sano': {'Sano': 0.7, 'Enfermo': 0.3},
    'Enfermo': {'Sano': 0.4, 'Enfermo': 0.6}
}

# Emisión P(Ot | Xt)
EMISION = {
    'Sano': {'Normal': 0.9, 'Fiebre': 0.1},
    'Enfermo': {'Normal': 0.2, 'Fiebre': 0.8}
}

# ====================== FILTRADO ======================================

def filtrar(secuencia_obs):
    belief = PI.copy()

    print("\n[DBN - Filtrado]\n")
    print("Inicial:", belief)

    for t, obs in enumerate(secuencia_obs):
        nuevo_belief = {}

        # 🔹 Predicción + actualización
        for estado_actual in ESTADOS:
            suma = 0

            for estado_prev in ESTADOS:
                suma += belief[estado_prev] * TRANSICION[estado_prev][estado_actual]

            nuevo_belief[estado_actual] = suma * EMISION[estado_actual][obs]

        # 🔹 Normalizar
        total = sum(nuevo_belief.values())
        for s in nuevo_belief:
            nuevo_belief[s] /= total

        belief = nuevo_belief

        print(f"\nTiempo {t} | Observación: {obs}")
        print("Creencia:", belief)

    return belief

# ====================== EJECUCIÓN =====================================

secuencia = ['Normal', 'Fiebre', 'Fiebre']
filtrar(secuencia)