'''
Red de decisión:
Ejemplo de llevar paraguas o no
'''

# ====================== PROBABILIDAD ================================

# Probabilidad de lluvia
P_lluvia = 0.3
P_no_lluvia = 0.7

# ====================== UTILIDADES ==================================

# utilidad(acción, clima)

utilidades = {
    'llevar': {
        'lluvia': 50,     # te proteges
        'no_lluvia': -10  # incomodidad
    },
    'no_llevar': {
        'lluvia': -100,   # te mojas
        'no_lluvia': 20   # cómodo
    }
}

# ====================== UTILIDAD ESPERADA ============================

def utilidad_esperada(accion):
    return (
        P_lluvia * utilidades[accion]['lluvia'] +
        P_no_lluvia * utilidades[accion]['no_lluvia']
    )

# ====================== DECISIÓN =====================================

def tomar_decision():
    acciones = ['llevar', 'no_llevar']
    resultados = {}

    for accion in acciones:
        ue = utilidad_esperada(accion)
        resultados[accion] = ue

    print("\nUtilidad esperada:")
    for a, v in resultados.items():
        print(f"{a}: {v:.2f}")

    mejor = max(resultados, key=resultados.get)
    print("\nMejor decisión:", mejor)

# ====================== EJECUCIÓN ====================================

tomar_decision()