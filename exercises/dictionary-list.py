'''
# diccionarios en listas

persons = []

person01 = {
    'name' : 'arturo', 
    'age': '21', 
    'city': 'mendoza'
    }

person02 = {
    'name' : 'martina',
    'age' : '21',
    'city' : 'mendoza'
}

person03 = {
    'name' : 'graciela',
    'age' : '52',
    'city' : 'mendoza'
}

persons = [person01, person02, person03]

for person in persons:
    print("Datos personales: ")
'''

# diccionarios en diccinarios

ciudades = {
    
    'tokio' : {
        'pais': 'japon',
        'poblacion': '14 millones',
        'curiosidades': 'rascacielos iluminados con neones'
    },

    'mendoza' : {
        'pais' : 'argentina',
        'poblacion' : '2 millones',
        'curiosidades' : 'la mejor produccion de vino' 
    },

    'cordoba' : {
        'pais' : 'argentina',
        'poblacion' : '3.8 millones',
        'curiosidades' : 'cuidad del fernet'
    },
}

for ciudad, info in ciudades.items():
    print(f"Ciudad: {ciudad.title()}")
    pais = f"{info['pais']}"
    poblacion = f"{info['poblacion']}"
    curiosidades = f"{info['curiosidades']}"

    print("Informacion: ")
    print(f"Pais: {pais.title()}")
    print(f"Poblacion: {poblacion}")
    print(f"Curiosidades: {curiosidades.title()}\n")