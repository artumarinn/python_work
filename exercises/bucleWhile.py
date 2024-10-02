# bucle while

pizza = "\nVamos a agregar ingredientes a tu pizza"
pizza += "\nColoca los ingredientes:  " 

while pizza:
    ingredientes = input(pizza)

    if ingredientes == 'quit':
        break
    else:
        print(f"Usted le agrego: {ingredientes}")

edad = "\nBienvenido al cine"
edad += "\nIngrese la edad:"

active = True
while active:
    edad = input(edad)
    edad = int(edad)

    if edad == 0:
        active = False
        if active == False:
            break

    if edad < 3:
        print("Gratis")
    elif edad > 3 and edad < 12:
        print("8 euros")
    else:
        print("12 euros")


# bucle infinito
number = 2
while number < 5:
    print(number)
