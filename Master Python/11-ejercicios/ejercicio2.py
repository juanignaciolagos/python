"""
Ejercicio2: mostrar un programa que añada valores a una lista mientras que su longitud sea menor a 120
y luego mostrarlo
"""
cont = 1
lista = []

print("### con For #####")

for cont in range(1,121):
    lista.append(cont)

print(lista)

print("### con While #####")

while cont < 121:
    lista.append(cont)
    
    cont += 1
  
print(lista)    
