first_name = "Arturo"
print(f"Hello, {first_name}, Would you like to learn python?")

print(f"{first_name.lower()}")
print(f"{first_name.upper()}")
print(f"{first_name.title()}")

print('Alber Einstein once said, “Don’t worry about your math problems, I can assure you that mine are bigger”')

famous_person = "Albert Einstein"
message = f'{famous_person} once said, “Don’t worry about your math problems, I can assure you that mine are bigger”'
print(message)

name = "\tArturo\t\nMarin"
print(name)
name = name.strip() # todos los espacios en blanco
print(name)
name = name.lstrip() # izquierda
print(name)
name = name.rstrip() # derecha 
print(name)

filename = 'python_notes.txt'
print(filename.removesuffix(".txt")) # mostrar nombre del archivo sin extencion de