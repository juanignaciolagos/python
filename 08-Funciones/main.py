"""
FUNCIONES:
    es un conjunto de instrucciones agrupadas bajo un nombre concreto que pueden reutilizarse invocando a la funcion tantas veces 
    como sea necesario

def Nombredemifuncion (parametros):
    #BLOQUE DE INSTRUCCIONES / CONJUNTO DE INSTRUCCIONES

Nombredemifuncion (mi_parametros)

"""

# ejemplo 1

print( "####################ejemplo1####################")

def muestranombre():
     print("juan")
     print("juan")
     print("juan")
     print("juan")
     print("juan")
     print("\n")

#invocar Funcion 

muestranombre()
muestranombre()


#ejemplo 2 parametros

print( "####################ejemplo2####################")

nombre = "juan" #input("introduce tu nombre: ")
edad = 27 #int(input("introduce tu edad: "))

def mostrartunombre (nombre,edad):
    
    print(f"tu nombre es: {nombre} ")
    if edad >=18:
        print("Y eres mayor de edad")


mostrartunombre(nombre,edad)

#ejemplo 3

print( "####################ejemplo 3####################")

numero =  1  #int(input("introduce el numero de tabla: "))

def tablamultiplicar (numero):
    print(F"##TABLA DEL {numero}##")
    
    for x in range(1,11):
        print(f"{numero}X{x}={numero*x}")

    print("\n")


tablamultiplicar(numero)
tablamultiplicar(3)
tablamultiplicar(6)
tablamultiplicar(9)

#ejemplo 3.1

for ntabla in range(1,11):
    tablamultiplicar(ntabla)
    
#ejemplo 4 

print( "####################ejemplo 3####################")
#parametros opcionales

def getempleado (nombre, DNI = None):
    print("Nombre Empleado")
    print(f"nombre empleado: {nombre}")
    if DNI != None:
        print(f"DNI empleado: {DNI}")

getempleado("juan")

# ejemplo 5 parametros opcionales y return o devolver datos de una funcion

print( "#################### ejemplo 5 ####################")

def saludame (nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo

print(saludame("Juan"))

print( "#################### ejemplo 6 ####################")

def calculadora (numero1, numero2, basicas = False):
    suma = numero1 + numero2 
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas == False:
        cadena = "suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:     
        cadena += "\n"
        cadena += "multiplicacion: " + str(multi)
        cadena += "\n"
        cadena += "Division: " + str(division)

    return cadena

print(calculadora(5,5,True))


print( "#################### ejemplo 7 ####################")

def getnombre (nombre):
    texto = f"El nombre es: {nombre}"

    return texto

def getapellidos (apellidos):
    texto = f"Los apellidos son: {apellidos}"

    return texto

def devuelvetodo (nombre, apellidos):
    texto = getnombre(nombre) + "\n" + getapellidos(apellidos)
    return texto

print(getnombre("Juan"),getapellidos("lagos"))
print(devuelvetodo("juan","lagos"))

print( "#################### ejemplo 8 ####################")

Dime_el_Year = lambda year: f"el año es: {year*23}"

print(Dime_el_Year(2034))