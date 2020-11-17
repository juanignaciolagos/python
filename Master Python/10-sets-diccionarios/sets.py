"""
sets es un tipo de datos para tener una coleeccion de valores pero,
no tiene ni indice ni orden
"""

personas = {
    "victor",
    "manolo",
    "francisco",
}

personas.add("paco")
personas.remove("francisco")

print(type(personas))
print(personas)