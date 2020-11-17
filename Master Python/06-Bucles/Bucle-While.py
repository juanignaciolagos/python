"""
# While

es una estrucutura de control que itera o repote la ejecución de una serie de instrucciones tantas veces como sea necesario, hasta que
deje de cumplirse esa condicion.

while condicion:
    Bloque de instrucciones
    actuañlizacion de contador

"""

contador = 1

while contador <=100:
    print(f"EStoy en el numero: {contador}")
    contador += 1


print("----------------------------------------------------------------")

contador = 1
muestrame = str(0)

while contador <=500:
    muestrame = muestrame +","+str(contador)
    contador += 1

print(muestrame)

print("####################################ejemplo##################################")

numero_usuario = int(input("de que numero quieres la tabla: "))

if numero_usuario <1:
    numero_usuario =1

print(f"##tabla del numero: {numero_usuario}")

contador = 1

while contador <=10:
    print(f"multiplica {numero_usuario}X{contador}={numero_usuario*contador}")
    contador += 1
else:
    print("Tabla Terminada")