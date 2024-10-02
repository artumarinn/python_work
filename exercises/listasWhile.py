pedidos_bocadillos = ['pastrami', 'jamon y queso', 'salame y queso', 'pastrami', 'milanesa', 'pastrami']
bocadillos_terminados = []

print("Pedidos de bocadillos: ")
for pedido_bocadillo in pedidos_bocadillos:
    print(pedido_bocadillo.title())
    
print("\nNo queda pastrami, asi que no podremos hacerlos")
while 'pastrami' in pedidos_bocadillos:
    pedidos_bocadillos.remove('pastrami')

print("\nPedidos de bocadillos: ")
for pedido_bocadillo in pedidos_bocadillos:
    print(pedido_bocadillo.title())


while pedidos_bocadillos:
    pedidos_actuales = pedidos_bocadillos.pop()

    print(f"Haciendo pedido de {pedidos_actuales.title()}")
    bocadillos_terminados.append(pedidos_actuales)

    print("\nBocadillos terminados: ")
    for bocadillo_terminado in bocadillos_terminados:
        print(bocadillo_terminado.title())


# Vacaciones de ensueño




