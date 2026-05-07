'''
Probabilidad condicionada y normalización
'''

# ====================== DATOS =========================================

# Total de días
total = 100

# Eventos
lluvia = 30
nubes = 40
lluvia_y_nubes = 25

# ====================== PROBABILIDAD CONDICIONADA =====================

# P(Lluvia | Nubes)
P_lluvia_dado_nubes = lluvia_y_nubes / nubes

print("\nProbabilidad condicionada:\n")
print("P(Lluvia | Nubes) =", round(P_lluvia_dado_nubes, 3))

# ====================== NORMALIZACIÓN ================================

print("\nNormalización:\n")

valores = {
    'A': 2,
    'B': 3,
    'C': 5
}

suma = sum(valores.values())

probabilidades = {}

for k in valores:
    probabilidades[k] = valores[k] / suma

# Mostrar resultados
for k in probabilidades:
    print(f"P({k}) = {probabilidades[k]:.3f}")

print("\nSuma total =", sum(probabilidades.values()))