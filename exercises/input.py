coche = input("Que coche desea alquilar?: ")
print(f"Veamos si tenemos un {coche.title()} para usted")


personas = input("Cuantos vienen a cenar?: ")
personas = int(personas)

if personas > 8:
    print("Me temo que deberan esperar una mesa")
else:
    print("Muy bien, su mesa esta lista")


number = input("Ingrese un numeromultiplo de 10: ")
number = int(number)

if number % 10 == 0:
    print("Su numero es multiplo de 10!")
else:
    print("Su numero no es multiplo de 10")

