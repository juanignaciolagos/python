"""
proyecto pyhton y mysql:
-login o registro
-si elegimos registro creara un usuario en la BBDD
-si elegimos login identificara al usuario y nos preguntara
-crear nota mostrar notas y borrarlas
"""
from usuarios import acciones

print("""
Acciones disponibles:
    -registro
    -login

""")

objeto = acciones.Acciones()

accion = input("¿que quieres hacer?: ")

if accion == "registro":
    objeto.registro()

elif accion == "login":
    objeto.login()

