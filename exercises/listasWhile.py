pedidos_bocadillos = ['jamon y queso', 'salame y queso', 'milanesa']
bocadillos_terminados = []

while pedidos_bocadillos:
    pedidos_actuales = pedidos_bocadillos.pop()

    print(f"Haciendo pedido de {pedidos_actuales.title()}")
    bocadillos_terminados.append(pedidos_actuales)

    print("Bocadillos terminados: ")
    for bocadillo_terminado in bocadillos_terminados:
        print(bocadillo_terminado.title())

