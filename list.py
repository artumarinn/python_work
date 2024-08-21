# Listas
bicycles = ['trek', 'cannondale', 'redline', 'specialiced']
print(bicycles[0].title()) # se imprime el primer elemento de la lista con la primera letra mayuscula

print(bicycles[-1]) # ultimo valor de la lista 

message = f"My first bicycle was a {bicycles[0]}"
print(message)

bicycles[2] = 'Topmega' # modificar un elemento de la lista 
bicycles.append('Giant') # agregar un elemento de la lista
bicycles.insert(0, 'Redline') # insertar elementos en cualquier posicion de la lista
print(bicycles)

del bicycles[0]
print(bicycles)

popped_bicycles = bicycles.pop() # eliminamos ultimo elemento de la lista pero se guardo en la varibale
print(popped_bicycles)

bicycles.remove('specialiced') # eliminar un elemento de la lista si no se sabe la el valor 
print(bicycles)

