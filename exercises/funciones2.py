"""
def hacer_camiseta(talla, texto):
    print(f"La talla de la camiseta es {talla} y que dice: {texto}")

hacer_camiseta('XL', 'Aguante Boca')
hacer_camiseta(talla='M', texto='Argentina')
"""
# ---------------------------------------------------------------------
"""
def hacer_camiseta(talla='XXL', text='Me encanta Python'):
    print(f"La camiseta es de talla {talla} y dice {text}")

hacer_camiseta()
hacer_camiseta(talla='XL')
hacer_camiseta(text='Aguante Python')
"""
#----------------------------------------------------------------------

def describir_cuidades(nombre='Mendoza', pais='Argentina'):
    print(f"{nombre} esta en {pais}")

describir_cuidades()
describir_cuidades(nombre='Cordoba')
describir_cuidades(nombre='Buenos Aires')
describir_cuidades(nombre='Montevideo', pais='Uruguay')
