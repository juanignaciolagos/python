"""
Escribir un Script que nos muestre por pantalla todos los numero partes del 1 al 120 

"""

print("#################forma 1##################")

contador = 1

for contador in range(1,121):
    if contador%2 == 0:
        print(contador)


print("#################forma 2##################")

contador = 2
muestrame = ""

while contador < 121 :
    muestrame = muestrame + ", "+ str(contador)
    contador += 2

print(muestrame)
