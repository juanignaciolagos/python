"""
Crear una lista con el contenido de esta tabla:
accion      aventura            deporte 
GTA         assins              FIFA
COD         crash               PRO
PUGB        Prince of persia    moto GP

mostrar esta informacion ordenada (crear diccionario)
"""

Tabla = [
    {
        "categoria:":"accion",
        "juegos": ["GTA","COD","PUGB"]
    },
    {
        "categoria:":"aventura",
        "juegos": ["assins","crash","Prince of persia"]
    },
    {
        "categoria:":"deporte",
        "juegos": ["FIFA","PRO","moto GP"]
    }
]

for categoria in Tabla:
    print(f"------------------------{categoria['categoria:']}--------------------------------")
    for juego in categoria['juegos']:
        print(f"---{juego}")