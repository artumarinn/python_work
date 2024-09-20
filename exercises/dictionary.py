person = {
    'name' : 'arturo', 
    'age': '21', 
    'city': 'mendoza'
    }

for key, value in person.items():
    print(f"{key}: {value.title()}")

favorite_lenguage = {
    'sarah': 'python',
    'jed': 'java',
    'edward': 'rust',
    'arturo': 'python'
}

for name, lenguage in favorite_lenguage.items():
    print(f"{name.title()}'s favorite lenguage is {lenguage.title()}")
    
if 'jed' in favorite_lenguage.keys(): # keys busca en el diccionario la clave
        print("GREAT!")

for name in sorted(favorite_lenguage.keys()): # orden las claves 
    print(f"{name}")

for lenguage in set(favorite_lenguage.values()): # set utiliza la "coleccion" de valores unicos, no imprime duplicados
     print(f"{lenguage}")


