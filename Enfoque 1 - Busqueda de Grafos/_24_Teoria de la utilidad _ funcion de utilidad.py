'''
Teoría de la utilidad:
Decisión basada en utilidad esperada
'''

# ====================== OPCIONES =======================================

# Cada acción tiene resultados posibles: (probabilidad, utilidad)
opciones = {
    'Invertir': [
        (0.7, 100),   # gana dinero
        (0.3, -50)    # pierde dinero
    ],
    'Ahorrar': [
        (1.0, 30)     # ganancia segura
    ],
    'Gastar': [
        (1.0, 60)     # satisfacción inmediata
    ]
}

# ====================== FUNCIÓN DE UTILIDAD ============================

def utilidad(x):
    """
    Función de utilidad (puede ser no lineal)
    Ejemplo: aversión al riesgo (raíz cuadrada)
    """
    if x >= 0:
        return x ** 0.5
    else:
        return -((-x) ** 0.5)

# ====================== UTILIDAD ESPERADA ==============================

def utilidad_esperada(opcion):
    total = 0
    for prob, resultado in opcion:
        total += prob * utilidad(resultado)
    return total

# ====================== DECISIÓN =======================================

def elegir_mejor(opciones):
    resultados = {}

    for nombre, opcion in opciones.items():
        ue = utilidad_esperada(opcion)
        resultados[nombre] = ue

    print("\nUtilidades esperadas:")
    for op, val in resultados.items():
        print(f"{op}: {val:.4f}")

    mejor = max(resultados, key=resultados.get)
    print("\nMejor decisión:", mejor)

# ====================== EJECUCIÓN ======================================

elegir_mejor(opciones)