'''
Independencia condicional
'''

# ====================== PROBABILIDADES ================================

# Evento C = estudiar
P_C = 0.8

# Evento A = aprobar matemáticas dado que estudió
P_A_dado_C = 0.9

# Evento B = aprobar física dado que estudió
P_B_dado_C = 0.85

# ====================== INDEPENDENCIA CONDICIONAL =====================

# Si A y B son independientes dado C:
P_AyB_dado_C = P_A_dado_C * P_B_dado_C

# ====================== RESULTADOS ====================================

print("\nIndependencia condicional:\n")

print("P(A | C) =", P_A_dado_C)
print("P(B | C) =", P_B_dado_C)

print("\nP(A y B | C) =")
print(f"{P_A_dado_C} × {P_B_dado_C}")

print("Resultado =", round(P_AyB_dado_C, 3))