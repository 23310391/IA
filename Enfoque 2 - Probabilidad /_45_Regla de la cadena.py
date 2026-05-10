'''
Red Bayesiana simple
'''

# ====================== VARIABLES =====================================

# P(Lluvia)
P_lluvia = 0.3

# P(Cesped mojado | Lluvia)
P_mojado_dado_lluvia = 0.9

# P(Cesped mojado | No lluvia)
P_mojado_dado_no_lluvia = 0.2

# ====================== PROBABILIDAD TOTAL ============================

P_no_lluvia = 1 - P_lluvia

# P(Cesped mojado)
P_mojado = (
    P_mojado_dado_lluvia * P_lluvia
    +
    P_mojado_dado_no_lluvia * P_no_lluvia
)

# ====================== BAYES =========================================

# P(Lluvia | Cesped mojado)
P_lluvia_dado_mojado = (
    P_mojado_dado_lluvia * P_lluvia
) / P_mojado

# ====================== RESULTADOS ====================================

print("\nRed Bayesiana:\n")

print("P(Lluvia) =", P_lluvia)

print("\nP(Cesped mojado) =", round(P_mojado, 3))

print("\nP(Lluvia | Cesped mojado) =")
print(round(P_lluvia_dado_mojado, 3))