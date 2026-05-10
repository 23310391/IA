'''
Eliminación de variables
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

# ====================== FACTOR ========================================

def factor_mojado(mojado=True):
    factor = {}

    for lluvia in [True, False]:

        # P(Mojado | Lluvia)
        if mojado:
            p_mojado = P_mojado_dado_lluvia[lluvia]
        else:
            p_mojado = 1 - P_mojado_dado_lluvia[lluvia]

        factor[lluvia] = (
            P_lluvia[lluvia] * p_mojado
        )

    return factor

# ====================== ELIMINACIÓN ===================================

def eliminar_variable(factor):
    return sum(factor.values())

# ====================== INFERENCIA ====================================

# Crear factor
factor = factor_mojado(True)

# Eliminar variable oculta
P_mojado = eliminar_variable(factor)

# Probabilidad posterior
P_lluvia_dado_mojado = (
    factor[True] / P_mojado
)

# ====================== RESULTADOS ====================================

print("\nEliminación de variables:\n")

print("Factor:")
print(factor)

print("\nP(Mojado) =", round(P_mojado, 3))

print("\nP(Lluvia | Mojado) =")
print(round(P_lluvia_dado_mojado, 3))