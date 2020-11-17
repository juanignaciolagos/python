"""
ejercicio1. hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:
-recorrer la lista y mostrarla
-hacer funncion que recorra listas de numero y devuelva un string
-ordenarla y mostrarla
-mostrar su longitud
-buscar algun elemento (que el usuario pida por teclado)
"""

lista = [8,7,6,5,4,3,2,1]

print("##### Recorrer lista y mostrar ejemplo curso #####")
for x in lista:
    print(x)

print("##### Recorrer lista y mostrar #####")
for x in lista:
    print(f"el numero de la lista es: {x}")

lista.sort()

print("##### hacer funncion que recorra listas de numero y devuelva un string ejemplo curso #####")
def mostrar_lista(numeros):
    resultado = ""
    for x in lista:
        resultado += str(x)
        resultado += "\n"
    return resultado

print(mostrar_lista(lista))

print("##### hacer funncion que recorra listas de numero y devuelva un string #####")
def mostrarlista(numero):
    numero = ""
    for y in lista:
        numero += "elemento: " + str(y)
        numero += "\n"
    
    return numero

print(mostrarlista(lista))


print("##### ordenarla y mostrarla #####")
lista.sort()
for x in lista:
    print(f"el numero de la lista es: {x}")

print("##### mostrar su longitud #####")
print(len(lista))

try:
    print("##### busqueda en la lista #####")

    busqueda = int(input("introduce el numero: "))

    comprobar = isinstance(busqueda, int)

    while not comprobar or busqueda <=0:
        busqueda = int(input("introduce el numero: "))
    else:
        print(f"has introducido el {busqueda}")

    print(f"### buscar en la lista el numero {busqueda} ###")


    search = lista.index(busqueda)
    print(f" el numero buscado existe en la lista, es el indice: {search}")
except:
    print("el numero no esta en la lista")
