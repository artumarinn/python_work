"""def ciudad_pais(ciudad, pais):
    print(f"{ciudad}, {pais}")

ciudad_pais('Mendoza', 'Argentina')
ciudad_pais(ciudad='Santiago', pais='Chile')
ciudad_pais('Bogota', 'Colombia')"""

#-------------------------------------------------

def hacer_album(artista, titulo_album, nro_canciones= None):
    album = {'nombre_artista': artista, 'nombre_album': titulo_album, 'canciones': nro_canciones }
    return album

albums = []

while True:
    print("Datos del Album:")
    nombre_artista = input("Nombre del artista('q' para salir): ")
    if nombre_artista == 'q':
        break

    nombre_album = input("Nombre del album('q' para salir): ")
    if nombre_album == 'q':
        break

    canciones = input("Nuero de canciones('q' para salir): ")
    if canciones == 'q':
        break

    nuevo_album = hacer_album(nombre_artista, nombre_album, canciones)
    albums.append(nuevo_album)
    print(nuevo_album)
    

print("Albunes Creados: ", albums)

    

"""
primer_album = hacer_album(artista='2pac', titulo_album='All eyez on me')
print(primer_album)
segundo_album = hacer_album(artista='Gustavo Ceratti', titulo_album='Ahi vamos', nro_canciones='13 canciones')
print(segundo_album)


"""