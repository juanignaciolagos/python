"""
muestrame los cuadrados de los primeros 60 numeros naturales
resolverlo con for y while
"""

#while 

print("###########ejemplo 1################")

numero = 0

while numero <=60:
    
    cuadrado = numero*numero
    print(f"{numero}: {cuadrado}")
    numero += 1


#for
print("\n###################ejemplo 2#####################")

for numero in range(1,61):

    cuadrado = numero*numero
    
    print(f"{numero}: {cuadrado}")