'''
Modelo Oculto de Markov (HMM)
Algoritmo Forward
'''

# ====================== ESTADOS Y OBSERVACIONES =======================

ESTADOS = ['Concentrado', 'Distraido']
OBSERVACIONES = ['leer', 'usar_celular', 'escribir']

# ====================== PROBABILIDADES ================================

# Probabilidades iniciales
PI = {
    'Concentrado': 0.6,
    'Distraido': 0.4
}

# Transición P(s_t | s_{t-1})
TRANSICION = {
    'Concentrado': {'Concentrado': 0.7, 'Distraido': 0.3},
    'Distraido': {'Concentrado': 0.4, 'Distraido': 0.6}
}

# Emisión P(obs | estado)
EMISION = {
    'Concentrado': {
        'leer': 0.5,
        'usar_celular': 0.1,
        'escribir': 0.4
    },
    'Distraido': {
        'leer': 0.1,
        'usar_celular': 0.6,
        'escribir': 0.3
    }
}

# ====================== FORWARD =======================================

def forward(secuencia):
    alpha = []

    # 🔹 Paso 1: inicialización
    alpha_0 = {}
    for estado in ESTADOS:
        alpha_0[estado] = PI[estado] * EMISION[estado][secuencia[0]]
    alpha.append(alpha_0)

    # 🔹 Paso 2: recursión
    for t in range(1, len(secuencia)):
        alpha_t = {}
        for estado_actual in ESTADOS:
            suma = 0
            for estado_prev in ESTADOS:
                suma += (
                    alpha[t-1][estado_prev] *
                    TRANSICION[estado_prev][estado_actual]
                )
            alpha_t[estado_actual] = suma * EMISION[estado_actual][secuencia[t]]
        alpha.append(alpha_t)

    # 🔹 Paso 3: terminación
    prob_total = sum(alpha[-1].values())

    # Mostrar resultados
    print("\n[HMM - Forward]\n")
    for t, paso in enumerate(alpha):
        print(f"Tiempo {t}: {paso}")

    print("\nProbabilidad total de la secuencia:", prob_total)

# ====================== EJECUCIÓN =====================================

secuencia = ['leer', 'usar_celular', 'escribir']
forward(secuencia)