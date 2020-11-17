"""
LISTAS (arrays)
colecciones de datos bajo un unico nombre 
para accerder a estos valores podemos usar un indice numerico.
"""

pelicula = "batman"

#definir listas
peliculas = ["batman","Spiderman","El señor de los anillos"] 
cantantes = list(("2pac","drake","jennifer lopez"))
years = list(range(2020,2050))
variada = ["juan",30,4.4,True,"texto"]

"""
print(pelicula)
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""

#indices
pelicula = "otra cosa"
peliculas[1] = "gran torino"

print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:3])
print(peliculas[2:])

#agregar contenidos a una lista

cantantes.append("kase O")
cantantes.append("natos y waor")
print(cantantes)

# recorrer lista


"""
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("introduce la nueva pelicula: ")
    if nueva_pelicula != "parar":
         peliculas.append(nueva_pelicula)
"""

print("\n##### listado peliculas#####")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")

#listas multidimensionales

print("\n************* listado de contactos**************")
contactos = [
    [
     "antonio",
     "antonio@antonio.com"
    ],
    [
        "luis",
        "luis@luis.com"
    ],
    [
        "Salvador",
        "salvador@salvador.com"
    ],
]

for contacto in contactos:
    for x in contacto:
        if contacto.index(x) ==0:
            print("Nombre: "+ x)
        else:
            print("E-mail: "+ x)
    print("\n")


#print(contactos[1][0])

