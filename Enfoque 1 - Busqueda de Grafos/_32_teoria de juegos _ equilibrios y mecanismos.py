'''
Mecanismo: Subasta de segundo precio
'''

def subasta_vickrey(ofertas):
    # ordenar ofertas de mayor a menor
    ordenadas = sorted(ofertas.items(), key=lambda x: x[1], reverse=True)

    ganador = ordenadas[0][0]
    mejor_oferta = ordenadas[0][1]
    segundo_precio = ordenadas[1][1]

    print("\nSubasta Vickrey:")
    print("Ofertas:", ofertas)
    print("Ganador:", ganador)
    print("Paga:", segundo_precio)

# Ejemplo
ofertas = {
    'Agente1': 100,
    'Agente2': 80,
    'Agente3': 60
}

subasta_vickrey(ofertas)