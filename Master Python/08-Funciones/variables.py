
"""
#Variables locales: son las que se definen dentro de una funcion y no se pueden usar fuera de ella, 
#solo estan disponibles dentro.
#a no ser que hagamos un return

#Variables Globales: son las que se declaran fuera de la funcion y estan disponibles dentro y fuera de ellas
"""


frase = "ni los genios son tan genios, ni los mediocres tan mediocres"

print(frase)

def holamundo ():
    frase = "hola mundo"
    print("dentro de la funcion")
    print(frase)
    year = 2021
    print(year)

    global website 
    website = "victorrobles.es"
    print("dentro:", website)
    return "dato devuelto" + str(year)



print(holamundo())
holamundo()
print(website)