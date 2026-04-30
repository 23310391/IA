'''
Valor de la Información (VOI) 
'''

# ====================== PROBABILIDADES ===============================

P_lluvia = 0.3
P_no_lluvia = 0.7

# ====================== UTILIDADES ==================================

utilidades = {
    'llevar': {
        'lluvia': 50,
        'no_lluvia': -10
    },
    'no_llevar': {
        'lluvia': -100,
        'no_lluvia': 20
    }
}

# ====================== UTILIDAD ESPERADA ============================

def utilidad_esperada(accion):
    return (
        P_lluvia * utilidades[accion]['lluvia'] +
        P_no_lluvia * utilidades[accion]['no_lluvia']
    )

# ====================== SIN INFORMACIÓN ==============================

def mejor_sin_info():
    acciones = ['llevar', 'no_llevar']
    resultados = {a: utilidad_esperada(a) for a in acciones}
    
    mejor = max(resultados, key=resultados.get)
    return mejor, resultados[mejor], resultados

# ====================== CON INFORMACIÓN PERFECTA =====================

def con_info_perfecta():
    # Mejor decisión si llueve
    if utilidades['llevar']['lluvia'] > utilidades['no_llevar']['lluvia']:
        mejor_lluvia = 'llevar'
    else:
        mejor_lluvia = 'no_llevar'

    # Mejor decisión si no llueve
    if utilidades['llevar']['no_lluvia'] > utilidades['no_llevar']['no_lluvia']:
        mejor_no_lluvia = 'llevar'
    else:
        mejor_no_lluvia = 'no_llevar'

    utilidad_lluvia = utilidades[mejor_lluvia]['lluvia']
    utilidad_no_lluvia = utilidades[mejor_no_lluvia]['no_lluvia']

    utilidad_total = (
        P_lluvia * utilidad_lluvia +
        P_no_lluvia * utilidad_no_lluvia
    )

    return mejor_lluvia, mejor_no_lluvia, utilidad_total

# ====================== VALOR DE LA INFORMACIÓN ======================

def calcular_voi():
    # Sin info
    mejor_accion, sin_info, resultados = mejor_sin_info()

    # Con info
    decision_lluvia, decision_no_lluvia, con_info = con_info_perfecta()

    voi = con_info - sin_info

    # 🔹 Mostrar resultados
    print("\n--- SIN INFORMACIÓN ---")
    for a, v in resultados.items():
        print(f"{a}: {v:.2f}")
    print("Mejor decisión:", mejor_accion)
    print("Utilidad:", sin_info)

    print("\n--- CON INFORMACIÓN PERFECTA ---")
    print(f"Si llueve → {decision_lluvia}")
    print(f"Si no llueve → {decision_no_lluvia}")
    print("Utilidad esperada:", con_info)

    print("\n--- VALOR DE LA INFORMACIÓN ---")
    print("VOI:", voi)

# ====================== EJECUCIÓN ====================================

calcular_voi()