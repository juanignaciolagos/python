"""
programa que Comprueba si una variable esta vacia, y si esta vacia rellernarla con un texto en minuscula y mostrarlo en
mayuscula
"""

varvacia = ""

if varvacia == "":
    varvacia = "juan"
else:
    print("la variable tiene contenido")

print(varvacia.upper())


if len(varvacia.strip()) <= 0:
    varvacia = "juan"
else:
    print("la variable tiene contenido")


print(varvacia.upper())