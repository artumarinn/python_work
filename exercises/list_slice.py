
foods = ['pastel de papa', 'empanadas', 'milanesas', 'pizza']
print(f"Estos son los 3 primeros elementos de la lista: {foods[:3]}")
print(f"Estos elementos enstan en el medio de la lista: {foods[1:3]}")
print(f"Estos son los 3 ultimos elementos de la lista: {foods[-3:]}")

pizzas = ['muzzarela', 'fugazzeta', 'pepperoni']
friend_pizzas = pizzas[:]

pizzas.append('cuatro quesos')
friend_pizzas.append('Jamon')

print("Mis pizzas son: ")
for mypizza in pizzas:
    print(mypizza.title())

print("Las pizzas de mi amigo son: ")
for friendpizza in friend_pizzas:
    print(friendpizza.title())