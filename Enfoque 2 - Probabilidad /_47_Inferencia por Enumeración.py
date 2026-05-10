'''
Inferencia por enumeración
'''

# ====================== PROBABILIDADES ================================

# P(Lluvia)
P_lluvia = {
    True: 0.3,
    False: 0.7
}

# P(Mojado | Lluvia)
P_mojado_dado_lluvia = {
    True: 0.9,
    False: 0.2
}

# ====================== ENUMERACIÓN ==================================

def prob_mojado(mojado=True):
    total = 0

    # Enumerar todos los valores de lluvia
    for lluvia in [True, False]:

        # P(Lluvia)
        p_lluvia = P_lluvia[lluvia]

        # P(Mojado | Lluvia)
        if mojado:
            p_mojado = P_mojado_dado_lluvia[lluvia]
        else:
            p_mojado = 1 - P_mojado_dado_lluvia[lluvia]

        total += p_lluvia * p_mojado

    return total

# ====================== BAYES =========================================

# P(Mojado)
P_mojado = prob_mojado(True)

# P(Lluvia y Mojado)
P_lluvia_y_mojado = (
    P_lluvia[True] *
    P_mojado_dado_lluvia[True]
)

# P(Lluvia | Mojado)
P_lluvia_dado_mojado = (
    P_lluvia_y_mojado / P_mojado
)

# ====================== RESULTADOS ====================================

print("\nInferencia por enumeración:\n")

print("P(Mojado) =", round(P_mojado, 3))

print("\nP(Lluvia | Mojado) =")
print(round(P_lluvia_dado_mojado, 3))