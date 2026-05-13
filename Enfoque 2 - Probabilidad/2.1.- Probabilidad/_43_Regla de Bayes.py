'''
Regla de Bayes
Diagnóstico médico simple
'''

# ====================== PROBABILIDADES ================================

# P(Enfermo)
P_enfermo = 0.01

# P(Positivo | Enfermo)
P_positivo_dado_enfermo = 0.95

# P(Positivo | Sano)
P_positivo_dado_sano = 0.10

# ====================== COMPLEMENTOS ==================================

P_sano = 1 - P_enfermo

# ====================== PROBABILIDAD TOTAL ============================

P_positivo = (
    P_positivo_dado_enfermo * P_enfermo
    +
    P_positivo_dado_sano * P_sano
)

# ====================== BAYES =========================================

P_enfermo_dado_positivo = (
    P_positivo_dado_enfermo * P_enfermo
) / P_positivo

# ====================== RESULTADOS ====================================

print("\nRegla de Bayes:\n")

print("P(Enfermo) =", P_enfermo)
print("P(Positivo | Enfermo) =", P_positivo_dado_enfermo)

print("\nP(Positivo) =", round(P_positivo, 4))

print("\nP(Enfermo | Positivo) =")
print(round(P_enfermo_dado_positivo, 4))