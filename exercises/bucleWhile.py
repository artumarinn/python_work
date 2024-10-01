# bucle while

pizza = "\nVamos a agregar ingredientes a tu pizza"
pizza += "\nColoca los ingredientes:  " 

while pizza:
    ingredientes = input(pizza)

    if ingredientes == 'quit':
        break
    else:
        print(f"Usted le agrego: {ingredientes}")