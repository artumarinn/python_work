# funciones con listas
"""
def mostrar_mensajes(msj):
    for mensaje in msj:
        print(mensaje)
    
msj = [
    'hola, como estas?', 
    'buenos dias', 
    'buenas, que tal'
]
"""
mensajes_enviados = []

def enviar_mensajes(msj):
    print("Mensajes por enviar: ")
    for mensajes in msj:
        print(mensajes)
    
    print("\nMensajes enviados:")
    while True:
        mensajes_enviados = msj.pop()
        print(mensajes_enviados)
    
        if msj == []:
            break
msj = [
    'hola, como estas?', 
    'buenos dias', 
    'buenas, que tal'
]

enviar_mensajes(msj[:]) # se guarda una copia [:] de la lista para conservar los mensajes

print("\nMensajes por enviar: ")
for mensajes in msj:
    print(mensajes[:])

