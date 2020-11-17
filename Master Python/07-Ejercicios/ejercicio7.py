"""
entre dos numeros que el usuario ingrese mostrar solo los numeros impares

"""

numero1 = int(input("Introduce el numero 1: "))
numero2 = int(input("Introduce el numero 2: "))



if numero1 <= numero2:
    rango = range(numero1,numero2)
    for contador in rango:
        print( 2*contador )
else:
    rango = range(numero2,numero1)
    for contador in rango:
        print( 2*contador )