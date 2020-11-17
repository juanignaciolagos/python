"""
Si se cumple esta funcion 
se ejecuta un conjunto de instrucciones 
Si NO se cumple 
se ejecuta otro grupo

ejemplo python:

If condicion:

instrucciones

else: 

instrucciones

operadores de comparacion:

== igual 
!= diferente
< menor que
> mayor que 
<= menor o igual que 
>= mayor o igual que

operadores logicos:
and Y
or O
! negacion 
not no

"""

print("#############EJEMPLO N°1##############")
#input("adivina cual es mi color favorito ")
color = "rojo"

if color == "rojo": 
    print("wena wena") 
    print("ese es ") 
else:   
    print("ese no es mi color favorito")

print("\n#############EJEMPLO N°2##############")
#int(input("en que año estamos? "))
año = 2012

if año >= 2021:
    print("el año es mayor o igual a 2021")
else:
    print("el año es menor a 2021")

print("\n#############EJEMPLO N°3##############")

nombre = "juan lagos"
ciudad = "santiago"
continente = "sudamerica"
edad = 17
mayoria_edad = 18 

if edad >= mayoria_edad:
    print(f"{nombre} Es mayor de edad")
    if continente != "Europa":
        print(f"{nombre} No es Europeo")
    else:
        print(f"{nombre} Es Europeo")
        
else:
    print(f"{nombre} No es mayor de edad")
    if continente != "Europa":
        print(f"{nombre} No es Europeo")
    else:
        print(f"{nombre} Es Europeo")

print("\n#############EJEMPLO N°4##############")

dia = 6

"""

if dia == 1:
    print("lunes")
else:
    if dia == 2: 
        print("martes")
    else:
        if dia == 3:
                print("miercoles")
        else:
            if dia == 4:
                    print("jueves")
            else:
                if dia == 5:
                        print("viernes")
                else:
                    if dia ==6:
                            print("sabado")
                    else:
                            print("domingo")

"""

if dia == 1:
    print("lunes")
elif dia == 2:
    print("martes")
elif dia == 3:
    print("miercoles")
elif dia == 4:
    print("jueves")
elif dia == 5:
    print("viernes")
elif dia == 6:
    print("sabado")
else:
    print("domingo")

print("\n#############EJEMPLO N°5##############")
#int(input("introduce tu edad: "))
edad_minima = 18
edad_maxima = 65
edad = 27

if edad >= 18 and edad <=65:   
    print( "trabaja")
else:
    print("no trabaja")

print("\n#############EJEMPLO N°6##############")    

pais = input("introduce tu pais: ")

if pais == "Mexico" or pais == "españa" or pais == "colombia":
    print(f"{pais} este es un pais de habla hispana")
else:
    print(f"{pais} este no es un pais de habla hispana")